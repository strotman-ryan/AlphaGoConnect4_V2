from collections import defaultdict
import random
import math
import copy
import Result

#Train the montecarlo tree by running rollout on the "root"
#(whatever the current board state is - make a new tree node for this each turn)

class MonteCarloTreeSearch:

	def __init__(self, exploration_weight=1):
		self.rewards = defaultdict(int)
		self.visit_counts = defaultdict(int)
		self.children = dict()
		self.exploration_weight = exploration_weight
		
		
	#Choose the best move to make from this node
	def search(self, node):
		if node not in self.children:
			return node.find_random_child()
		
		def score(n):
			if self.visit_counts[n] == 0:
				return float("-inf") # don't select unseen moves
			return self.rewards[n] / self.visit_counts[n] # average reward
		
		return max(self.children[node], key=score)
		
	#Train tree for one iteration (expand, simulate, backpropogate)
	def rollout(self, node):
		path = self._select(node)
		leaf_node = path[-1]
		self.expand(leaf_node)
		reward = self.simulate(leaf_node)
		self.backpropogate(path, reward)
	
	#Find an unexplored descendent/move of node, return path to it
	def select(self, node):
		path = []
		while True:
			path.append(node)
			if node not in self.children or not self.children[node]:
				#current node is unexplored or a terminal node
				return path
			#finds unexplored children of current node, returns an arbitrary one if one exists
			unexplored = self.children[node] - self.children.keys()
			if unexplored:
				n = unexplored.pop()
				path.append(n)
				return path
			#If all child nodes have been explored, descend down the tree
			node = self.uct_select(node)
	
	#Populate children dict with the children of node
	def expand(self, node):
		if node in self.children: #if the node has been expanded already
			return
		self.children[node] = node.find_children()
		
	#Finds reward for a random simulation of the game if it was played out from node
	def simulate(self, node):
		invert_reward = True
		while True:
			if node.is_terminal():
				reward = node.reward()
				return 1 - reward if invert+reward else reward
			node = node.find_random_child()
			invert_reward = not invert_reward #reward inverted due to opposing players taking turns
	
	#send reward back to ancestors of leaf (along path)
	def backpropogate(self, path, reward):
		for node in reversed(path):
			self.vist_counts[node] += 1 
			self.rewards[node] += reward 
			reward = 1 - reward #invert reward due to opposing players taking turns
	
	#UCT - Upper Confidence Trees
	#selects a child, attempting to balance exploring new moves and 
	def uct_select(self, node):
		log_visits_vertex = math.log(self.visit_counts[node])
		
		#upper confidence bound for trees formula
		def uct(n):
			return ( self.rewards[n]/self.visit_counts[n] + 
				self.exploration_weight * 
				math.sqrt(log_visits_vertex/self.visit_counts[n])
			)
		
		return max(self.children[node], key=uct)

class TreeNode():
	def __init__(self, board, player, move = -1):
		self.board = board
		self.player = player #True if Player1, False if Player2
		self.move = move
		if (self.move != -1) #Default value for initializing the root
			board.ChangePlayerTurn()
			board.addPlayerMove(move)
		
	
	#returns a set of all possible successors (moves) from this state
	def find_children(self):
		moves = self.board.possibleMoves()
		children = set()
		for move in moves:
			new_board = copy.deepcopy(board)
			children.push(TreeNode(new_board, !self.player, move))
		return children
	
	#returns a random child from possible children
	def find_random_child(self):
		return random.choice(self.find_children())
		
	#Use the NN to predict the best child???
	def find_best_child(self):
		pass
	
	#Does the game end at this node?
	def is_terminal(self):
		board_state = self.board.EvaluateBoard()
		return board_state != Result.NotFinished
	
	#Determines the reward for this node (assuming terminal) 1: win, 0: loss, .5=tie
	def reward(self):
		board_state = self.board.EvaluateBoard()
		if (player and board_state = Result.Player1Win)
			return 1
		if (!player and board_state = Result.Player2Win)
			return 1
		if (board_state = Result.Tie)
			return .5
		return 0
	
		
	