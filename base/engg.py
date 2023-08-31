import pandas as pd

import numpy as np
import pickle
import tensorflow as tf

y_kmeans_1 = pickle.load(open('base\y_kmeans1_engg.pkl','rb'))
y_kmeans_2 = pickle.load(open('base\y_kmeans2_engg.pkl','rb'))
y_kmeans_3 = pickle.load(open('base\y_kmeans3_engg.pkl','rb'))
y_kmeans_4 = pickle.load(open('base\y_kmeans4_engg.pkl','rb'))
y_kmeans_5 = pickle.load(open('base\y_kmeans5_engg.pkl','rb'))

ct_engg = pickle.load(open('base\ct_engg.pkl','rb'))

engg_class = salary_pred = tf.keras.models.load_model("base\engg.h5") 

def engg_clusters(Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs):
    engg = {
        'Age':[Age],
        'Gender': [Gender] ,
        'Stream' : [Stream],
        'Internships':[Internships],
        'CGPA': [CGPA], 
        'Hostel': [Hostel],
        'HistoryOfBacklogs':[HistoryOfBacklogs],
    }

    if(engg['Hostel']==['Yes']):
        engg.update([('Hostel',[1])])
    if(engg['Hostel']==['No']):
        engg.update([('Hostel',[0])])
    
    engg = pd.DataFrame(engg)

    X = engg[['Internships','CGPA']]
    X = X.iloc[:,[0,1]].values
    Y = engg[['CGPA','HistoryOfBacklogs']]
    Y = Y.iloc[:,[0,1]].values
    Z = engg[['Internships','HistoryOfBacklogs']]
    Z = Z.iloc[:,[0,1]].values
    K = engg[['CGPA','Hostel']]
    K = K.iloc[:,[0,1]].values
    N = engg[['Age','HistoryOfBacklogs']]
    N = N.iloc[:,[0,1]].values

    result_1 = y_kmeans_1.predict(X)
    result_2 = y_kmeans_2.predict(Y)
    result_3 = y_kmeans_3.predict(Z)
    result_4 = y_kmeans_4.predict(K)
    result_5 = y_kmeans_5.predict(N)

    result = [result_1[0],result_2[0],result_3[0],result_4[0],result_5[0]]

    return result

def engg_place(Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs):
    engg = {
        'Age':[Age],
        'Gender': [Gender] ,
        'Stream' : [Stream],
        'Internships':[Internships],
        'CGPA': [CGPA], 
        'Hostel': [Hostel],
        'HistoryOfBacklogs':[HistoryOfBacklogs],
    }

    if(engg['Hostel']==['Yes']):
        engg.update([('Hostel',[1])])
    if(engg['Hostel']==['No']):
        engg.update([('Hostel',[0])])

    engg = pd.DataFrame(engg)

    engg = ct_engg.transform(engg)  

    result_prob=engg_class.predict(engg)
    result = str(tf.round(result_prob))

    if(result=='tf.Tensor([[0.]], shape=(1, 1), dtype=float32)'):
        result = 0
    if(result=='tf.Tensor([[1.]], shape=(1, 1), dtype=float32)'):
        result = 1
    
    print(result)
    result_perc = round(100 * (np.max(result_prob[0])), 2)

    print("result_percent",result_perc)
    
    results = [result_perc,result]

    return results