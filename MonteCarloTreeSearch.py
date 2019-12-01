from collections import defaultdict
import math

class MonteCarloTreeSearch:

	def __init__(self, exploration_weight=1):
		self.rewards = defaultdict(int)
		self.visit_counts = defaultdict(int)
		self.children = dict()
		self.exploration_weight = exploration_weight
		
	#Choose the best move to make from this node
	def choose(self, node):
		if node not in self.children:
			return node.find_random_child()
		
		def score(n);
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
	def __init__(self, game, move, parent=None):
		self.game = game
		self.move = move 
		self.expanded = False
		self.parent = parent
		self.children = {}
		self.child_priority = np.zeros([7])
		self.child_value = np.zeros([7])
		self.child_visits = np.zeros([7])
		self.action_index = []
		
	#Monte Carlo has three steps: Select, Expand/Evaluate and Backup
		
	#Select step - selects best un-expanded node or end game node
		def select(self):
			current = self
			while current.expanded:
				best_move = current.best_child()
				current = current.add_child(best_move)
			return current
	
	