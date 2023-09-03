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

def clusters(gender,ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p):
    data = {
        'gender':[gender],
        'ssc_p':[ssc_p/100],
        'ssc_b':[ssc_b],
        'hsc_p':[hsc_p/100],
        'hsc_b':[hsc_b],
        'hsc_s':[hsc_s],
        'degree_p':[degree_p/100],
        'degree_t':[degree_t],
        'workex':[workex],
        'etest_p':[etest_p/100],
        'specialisation':[specialisation],
        'mba_p':[mba_p],
    }


    if(data['specialisation']==['Marketing and HR']):
        data.update([('specialisation',[0])])
    if(data['specialisation']==['Marketing and Finance']):
        data.update([('specialisation',[1])])
    if(data['workex']==['No']):
        data.update([('workex',[0])])
    if(data['workex']==['Yes']):
        data.update([('workex',[1])])
    if(data['degree_t']==['Science and Tech']):
        data.update([('degree_t',[0])])
    if(data['degree_t']==['Commerce and Management']):
        data.update([('degree_t',[1])])
   
    print(data)
    data = pd.DataFrame(data)
    
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
    print(result_1[0])
    print(result_2[0])
    print(result_3[0])
    print(result_4[0])
    print(result_5[0])
    print('_______________________________________________________________________')



    # return [result_1,result   _2,result_3,result_4,result_5]
    # print(result_1,result_2,result_3,result_4,result_5)
    result = [result_1[0],result_2[0],result_3[0],result_4[0],result_5[0]]
    return result

def placement_status(gender,ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p):
    data = {
        'gender':[gender],
        'ssc_p':[ssc_p],
        'ssc_b':[ssc_b],
        'hsc_p':[hsc_p],
        'hsc_b':[hsc_b],
        'hsc_s':[hsc_s],
        'degree_p':[degree_p],
        'degree_t':[degree_t],
        'workex':[workex],
        'etest_p':[etest_p],
        'specialisation':[specialisation],
        'mba_p':[mba_p],
    }
    if(data['gender']==['Male']):
        data.update([('gender',['M'])])
    if(data['gender']==['Female']):
        data.update([('gender','F')])
    if(data['specialisation']==['Marketing and HR']):
        data.update([('specialisation',['Mkt&HR'])])
    if(data['specialisation']==['Marketing and Finance']):
        data.update([('specialisation',['Mkt&Fin'])])
    if(data['degree_t']==['Science and Tech']):
        data.update([('degree_t',['Sci&Tech'])])
    if(data['degree_t']==['Commerce and Management']):
        data.update([('degree_t',['Comm&Mgmt'])])

    data = pd.DataFrame(data)
    print("_____________________________________________________________________________")
    print(data)
    print("_____________________________________________________________________________")
    data=ct_c.transform(data)
    result_prob=mba_class.predict(data)
    result = str(tf.round(result_prob))

    if(result=='tf.Tensor([[0.]], shape=(1, 1), dtype=float32)'):
        result = 0
    if(result=='tf.Tensor([[0.]], shape=(1, 1), dtype=float32)'):
        result = 1
    
    result_perc = round(100 * (np.max(result_prob[0])), 2)

    print("result is",result)
    print("result percentage is",result_perc)

    return [result,result_perc]

def salary(gender,ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p):
    data = {
        'gender':[gender],
        'ssc_p':[ssc_p],
        'ssc_b':[ssc_b],
        'hsc_p':[hsc_p],
        'hsc_b':[hsc_b],
        'hsc_s':[hsc_s],
        'degree_p':[degree_p],
        'degree_t':[degree_t],
        'workex':[workex],
        'etest_p':[etest_p],
        'specialisation':[specialisation],
        'mba_p':[mba_p],
    }
    if(data['gender']==['Male']):
        data.update([('gender',['M'])])
    if(data['gender']==['Female']):
        data.update([('gender','F')])
    if(data['specialisation']==['Marketing and HR']):
        data.update([('specialisation',['Mkt&HR'])])
    if(data['specialisation']==['Marketing and Finance']):
        data.update([('specialisation',['Mkt&Fin'])])
    if(data['degree_t']==['Science and Tech']):
        data.update([('degree_t',['Sci&Tech'])])
    if(data['degree_t']==['Commerce and Management']):
        data.update([('degree_t',['Comm&Mgmt'])])

    data = pd.DataFrame(data)
    print('Salary')
    print("                                      ")
    print("                                      ")

    data=ct_r.transform(data)
    result = salary_pred.predict(data)

    result = np.array(result)
    result = scaler.inverse_transform(np.array(result).reshape(-1,1))
    result = result[0][0]
    return result
