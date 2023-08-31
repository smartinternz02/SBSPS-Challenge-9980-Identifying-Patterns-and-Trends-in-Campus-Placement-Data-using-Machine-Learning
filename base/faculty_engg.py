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

def engg_clusters(filepath):
    engg = pd.read_csv(filepath)

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

    result1=result2=result3=result4=result5=0
    for i in range(0,len(result_1)):
        result1 += result_1[i][0]
        result2 += result_2[i][0]
        result3 += result_3[i][0]
        result4 += result_4[i][0]
        result5 += result_5[i][0]

    result_1 = result1/(len(result1)+1)
    result_2 = result2/(len(result2)+1)
    result_3 = result3/(len(result3)+1)
    result_4 = result4/(len(result4)+1)
    result_5 = result5/(len(result5)+1)

    result = [result_1,result_2,result_3,result_4,result_5]

    return result

def engg_place(filepath):
    

    engg = pd.read_csv(filepath)

    engg = ct_engg.transform(engg)  

    result_prob=engg_class.predict(engg)

    result_probs=0
    for i in range(0,len(result_prob)):
        result_probs += result_prob[i][0]
    
    result_prob = result_probs/(len(result_prob)+1)

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