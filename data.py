import pandas as pd

L = ['Tim',10,10,10,10,10,10,10,5,6,7,200,30,230]  # this should create by the program
data = pd.read_csv('Data.csv') #read the current file
newdata = data.append(pd.Series(L,index=data.columns),ignore_index=True) #combine to the file

newdata.to_csv('Data.csv') #generate the file