import pandas as pd
import google.colab.drive as drive
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from google.colab import drive
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
df=pd.read_csv('./drive/MyDrive/Colab Notebooks/data/samsung.csv')
print(df)

df1 = df[[ 'close', 'start', 'high', 'low', 'volume', 'transactionPrice', 'capitalization']]

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(df1)
arr = scaler.transform(df1)
arr
df1 = pd.DataFrame(arr, columns=df1.columns)
df1

df_corr= df1.corr()
df_corr_sort= df_corr.sort_values('close')
df_corr_sort['close']


x_train_pre= df1.iloc[:,0:7]
y= df1['close'].values
x_train, x_test, y_train, y_test= train_test_split(x_train_pre,y,test_size=0.2)
print(x_test)

model=Sequential()
model.add(Dense(10,input_dim=7,activation='relu'))
model.add(Dense(30,activation='relu'))
model.add(Dense(40,activation='relu'))
model.add(Dense(1))
model.summary()

model.compile(loss='mean_squared_error',optimizer='adam',metrics=['mse'])

early_stopping_callback= EarlyStopping(monitor='val_loss', patience=20)

history= model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.25, verbose=1, callbacks= [early_stopping_callback])

real_prices=[]
pred_prices=[]
x_num=[]

n_iter=0
y_prediction = model.predict(x_test).flatten()
for i in range(25):
  real=y_test[i]
  prediction=y_prediction[i]
  print('real price: {}', 'expected price: {}'.format(real,prediction))
  real_prices.append(real)
  pred_prices.append(prediction)
  n_iter= n_iter+1
  x_num.append(n_iter)

plt.plot(x_num, pred_prices, label= 'expected')
plt.plot(x_num,real_prices,label= 'real')
plt.legend()
plt.show()
