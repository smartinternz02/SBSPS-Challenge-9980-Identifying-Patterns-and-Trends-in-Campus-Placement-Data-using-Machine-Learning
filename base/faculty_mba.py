import numpy as np
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
import pickle 

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from sklearn.ensemble import RandomForestRegressor

from sklearn.cluster import KMeans


camp = pd.read_csv('base\Placement_Data_Full_Class (1).csv')
camp.drop('sl_no',axis=1,inplace=True)

salary_pred = tf.keras.models.load_model("base\salary.h5")
mba_class = tf.keras.models.load_model("base\mba_classification.h5")
y_kmeans1 = pickle.load(open("base\y_kmeans1.pkl","rb"))
y_kmeans2 = pickle.load(open("base\y_kmeans2.pkl",'rb'))
y_kmeans3 = pickle.load(open("base\y_kmeans3.pkl",'rb'))
y_kmeans4 = pickle.load(open("base\y_kmeans4.pkl",'rb'))
y_kmeans5 = pickle.load(open("base\y_kmeans5.pkl",'rb'))

ct_c = pickle.load(open("base\ct_c.pkl",'rb'))
ct_r = pickle.load(open("base\ct_r.pkl",'rb'))
scaler = pickle.load(open('base\scaler.pkl','rb'))

cols = ['gender', 'ssc_b', 'hsc_b', 'hsc_s', 'degree_t', 'specialisation', 'status']

def clusters(filepath):
   
    data = pd.read_csv(filepath)    
    

    cols.append('workex')
    cols.remove('status')
    for i in cols:

        data[i].replace(list(camp[i].unique()),list(range(0,data[i].nunique())),inplace=True)

    data['status'].replace(['Placed','Not Placed'],[0,1],inplace=True)

    print(data)

    X = data[['ssc_p','hsc_p']]
    X = X.iloc[:,[0,1]].values
    print(X)
    Y = data[['degree_p','specialisation']]
    Y = Y.iloc[:,[0,1]].values
    Z = data[['workex','degree_t']]
    Z = Z.iloc[:,[0,1]].values
    K = data[['workex','specialisation']]
    K = K.iloc[:,[0,1]].values
    N = data[['workex','degree_p']]
    N = N.iloc[:,[0,1]].values


    print('Eroor in the line above 70')
    result_1 = y_kmeans1.predict(X)
    result_2 = y_kmeans2.predict(Y)
    result_3 = y_kmeans3.predict(Z)
    result_4 = y_kmeans4.predict(K)
    result_5 = y_kmeans5.predict(N)

    print('_______________________________________________________________________')
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)
    print(result_5)
    print('_______________________________________________________________________')


    result1=result2=result3=result4=result5=0
    for i in range(0,len(result_1)):
        result1 += result_1[i]
        result2 += result_2[i]
        result3 += result_3[i]
        result4 += result_4[i]
        result5 += result_5[i]
    
    print(result1)

    result_1 = result1/len(result_1)
    result_2 = result2/len(result_2)
    result_3 = result3/len(result_3)
    result_4 = result4/len(result_4)
    result_5 = result5/len(result_5)

    results  = [result_1,result_2,result_3,result_4,result_5]

    return results

def placement_status(filepath):
   

    data = pd.read_csv(filepath)   
    data=data.drop('status',axis=1) 
    data=data.drop('salary',axis=1) 
    print("_____________________________________________________________________________")
    print(data)
    print("_____________________________________________________________________________")
    data=ct_c.transform(data)
    result_prob=mba_class.predict(data)
    
    print(result_prob)
    result_probs=0
    for i in range(0,len(result_prob)):
        result_probs += result_prob[i][0]
    
    print(result_probs)
    result_prob = result_probs/(len(result_prob)+1)
    print(result_prob)
    result = str(tf.round(result_prob))

    print(result)
    if(result=='tf.Tensor(0.0, shape=(), dtype=float64)'):
        result = 0
    if(result=='tf.Tensor(1.0, shape=(), dtype=float64)'):
        result = 1
    
    result_perc = round(100 * (np.max(result_prob)), 2)

    print("result is",result)
    print("result percentage is",result_perc)

    return [result,result_perc]


def salary(filepath):
    
    data = pd.read_csv(filepath)
    print('Salary')
    print("                                      ")
    print("                                      ")

    data=ct_r.transform(data)
    result = salary_pred.predict(data)

    result_sal=0
    for i in range(0,len(result)):
        result_sal += result[i][0]
    
    result= result_sal/len(result)

    result = np.array(result)
    result = scaler.inverse_transform(np.array(result).reshape(-1,1))
    result = result[0][0]
    return result
