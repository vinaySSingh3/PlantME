import pandas as pd
import numpy as np
import csv
from pandas import read_csv
from matplotlib import pyplot
df=pd.DataFrame()

#given values
state_number=96
#state_name='Thane'
corp_no=2   # 2 =rice



        
def cal():
    x = range(96, 121, 1)
    for state_number in x:
        df = pd.read_csv('Yield.csv')
        df.RandomForest== df.RandomForest.astype(float)  #more accurate
        #df.LinearRegression== df.LinearRegression.astype(float) #not using LinearRegrssion

        
        df=df[df.state_number==state_number]
        df2=df.sort_values(by='RandomForest',ascending=False)
        #print(df2)
        
        
        
        for i in range(1,6,1):
            df3=df2.iloc[[i]]
            df_state=df3['state_number'].to_string(index=False)
            df_crop=df3['crop_name'].to_string(index=False)
            df_RF=df3['RandomForest'].to_string(index=False)
            print(df_RF)
            print(df_state)

            f= open("Top5.csv", "a", newline="")

            #tup1 = (state_name,df2,rmse_rf,rmse_lr)
            
            tup1 = (df_state,df_crop,df_RF)
            writer= csv.writer(f)
            writer.writerow(tup1)
            f.close()
            state_number +=1


#cal()
#run this to get top 5 yields
        
        
        
        
        
        
        
    
