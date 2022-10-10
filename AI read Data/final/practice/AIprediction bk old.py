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

def AI_write():
    state_number=96
    corp_no=2
    x = range(1, 121-96, 1)
    for corp_no in x:
        AI_Cal(state_number,corp_no)
        state_number += 1
    
    

def AI_Cal(state_number,corp_no):

    x = range(2, 32, 1)
    for corp_no in x:
    
        df = pd.read_csv('bk1.csv',index_col='Year')
        #df=df.loc[df['DistName'] == state_name]
        #df=df[df.DistName==state_name]
        df=df[df.DistCode==state_number]

        df2=df.columns      #to get the column name
        df2=df2[corp_no]
        
        df=df.iloc[:,[0,corp_no]]
        df.head()
        df.plot(figsize=(12,8))
        

        df['1YearYield']=df[df2].shift(+1)
        df['2YearYield']=df[df2].shift(+2)
        df['3YearYield']=df[df2].shift(+3)
        
        #df['4YearYield']=df[df2].shift(+4)
        #df['5YearYield']=df[df2].shift(+5)
        #df['6YearYield']=df[df2].shift(+6)
        #df['7YearYield']=df[df2].shift(+7)
        #df['8YearYield']=df[df2].shift(+8)
        df=df.dropna()

        from sklearn import linear_model
        
        from sklearn.linear_model import LinearRegression
        lin_model=LinearRegression()

        from sklearn.ensemble import RandomForestRegressor
        model=RandomForestRegressor(n_estimators=100,max_features=3, random_state=1)

        x1,x2,x3,y=df['1YearYield'],df['2YearYield'],df['3YearYield'],df[df2]
        x1,x2,x3,y=np.array(x1),np.array(x2),np.array(x3),np.array(y)
        x1,x2,x3,y=x1.reshape(-1,1),x2.reshape(-1,1),x3.reshape(-1,1),y.reshape(-1,1)
        final_x=np.concatenate((x1,x2,x3),axis=1)

        #x1,x2,x3,x4,x5,x6,x7,x8,y=df['1YearYield'],df['2YearYield'],df['3YearYield'],df['4YearYield'],df['5YearYield'],df['6YearYield'],df['7YearYield'],df['8YearYield'],df[df2]
        #x1,x2,x3,x4,x5,x6,x7,x8,y=np.array(x1),np.array(x2),np.array(x3),np.array(x4),np.array(x5),np.array(x6),np.array(x7),np.array(x8),np.array(y)
        #x1,x2,x3,x4,x5,x6,x7,x8,y=x1.reshape(-1,1),x2.reshape(-1,1),x3.reshape(-1,1),x4.reshape(-1,1),x5.reshape(-1,1),x6.reshape(-1,1),x7.reshape(-1,1),x8.reshape(-1,1),y.reshape(-1,1)
        #final_x=np.concatenate((x1,x2,x3,x4,x5,x6,x7,x8),axis=1)
        #print(final_x)

        X_train,X_test,y_train,y_test=final_x[:-3],final_x[-3:],y[:-3],y[-3:]
        model.fit(X_train,y_train)
        lin_model.fit(X_train,y_train)
        
        
        pred=model.predict(X_test)
        import matplotlib.pyplot as plt
        plt.rcParams["figure.figsize"] = (12,8)
        plt.plot(pred,label='Random_Forest_Predictions')
        plt.plot(y_test,label='Actual YIELD')
        plt.legend(loc="upper left")
        #plt.show()

        
        lin_pred=lin_model.predict(X_test)
        import matplotlib.pyplot as plt
        plt.rcParams["figure.figsize"] = (12,8)
        plt.plot(lin_pred,label='Linear_Regression_Predictions')
        plt.plot(y_test,label='Actual YIELD')
        plt.legend(loc="upper left")
        #plt.show()
            
        
        #reg= linear_model.LinearRegression()

        
        #reg.fit(df[['pred_line']],df.
        #RiceYD = df_op.RiceYD
        #pred_line = df_op.RiceYD
        #reg.fit(df_op,RiceYD)
        #reg.predict('2018')

        from sklearn.metrics import mean_squared_error  
        from math import sqrt
        rmse_rf=sqrt(mean_squared_error(pred,y_test))
        rmse_lr=sqrt(mean_squared_error(lin_pred,y_test))

        print('Mean Squared Error for Random Forest Model is:',rmse_rf)
        print('Mean Squared Error for Linear Regression Model is:',rmse_lr)


        import csv
        f= open("Yield.csv", "a", newline="")
        #tup1 = (state_name,df2,rmse_rf,rmse_lr)
        tup1 = (state_number,df2,rmse_rf,pred[0],rmse_lr,lin_pred[0])
        writer= csv.writer(f)
        writer.writerow(tup1)
        f.close()

AI_write()

'''            

    dt.to_csv('file_name.csv',columns=[df[df2]])
    filename = "bk1.csv"

    import csv
    from itertools import islice

    with open(filename, 'r') as csv_in, open('output.csv', 'w', newline='') as csv_out:
    data = csv.reader(islice(csv_in, 5, None), delimiter=',')
    writer = csv.writer(csv_out)
    for row in data:
    print (row)
    writer.writerow(row)
'''



