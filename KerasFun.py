#See if a NN can determine winner




from keras.models import Sequential
from keras.layers import Dense
from keras import losses
import pandas as pd
from sklearn.model_selection import train_test_split



#import data
dataX = pd.read_csv("tic-tac-toe.csv",header= None)
dataX = dataX.replace(to_replace = 'x',value=1)
dataX = dataX.replace(to_replace = 'b',value=0)
dataX = dataX.replace(to_replace = 'o',value=0)
dataX.drop(columns = 9,inplace = True)
dataO = pd.read_csv("tic-tac-toe.csv",header= None)
dataO = dataO.replace(to_replace = 'x',value=0)
dataO = dataO.replace(to_replace = 'b',value=0)
dataO = dataO.replace(to_replace = 'o',value=1)
data = pd.concat([dataX,dataO],axis = 1)
data.columns = [x for x in range(19)]
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,0:17], data.iloc[:,18], test_size=0.05, random_state=42)

#make NN, one layer of 20 nuerons
model = Sequential()
model.add(Dense(units=50,activation='relu',input_dim=17))
#model.add(Dense(units=10,activation='relu',input_dim=17))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss=losses.mean_squared_error,optimizer='sgd',metrics=['accuracy'])

model.fit(X_train,y_train, epochs = 1500)
loss_and_metrics = model.evaluate(X_test, y_test)

#print(data.iloc[:,0:8])
#print(data.iloc[:,9])

