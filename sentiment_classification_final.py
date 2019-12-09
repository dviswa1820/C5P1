"""
@author: dviswa1820
"""
import io
import numpy as np
import pandas as pd
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
df=pd.DataFrame()
list1=list()
list2=list()
with open("C:\\Users\\Me\\Downloads\\sentiment labelled sentences (1)\\sentiment labelled sentences\\amazon_cells_labelled.txt",'r') as f1:
   with open("C:\\Users\\Me\\Documents\\X_train.txt",'w') as f3:
    f2=f1.readlines()
    for item in f2:
     
     tokens=nltk.word_tokenize(item)
     tokens1=tokens[:len(tokens)-2]
     senti1=re.compile(r'\d$')
     senti2=senti1.findall(item)
     list2.append(int(senti2[0]))
     i=0
     new_token=""
     for j in tokens1:
         new_token=(new_token+' '+str(j))
     new_token=new_token.strip()    
     #print(new_token)
     list1.append(new_token)
     f3.write(new_token+"\n")
     df=pd.concat([df,pd.DataFrame([[new_token,str(senti2[0])]])],axis=0,ignore_index=True)
     
   f3.close()     
f1.close()
with open("C:\\Users\\Me\\Documents\\X_train.txt", 'r') as f4:
    total=f4.readlines()
f4.close()    
X_train=np.asarray(list1[:399])
X_test=np.asarray(list1[401:499])
y_train=np.asarray(list2[:399])
y_test=np.asarray(list2[401:499])
print("*******************train*****************\n")
print(y_train.shape) 
print("*******************test*****************\n")
print(y_test.shape) 
count_vect=CountVectorizer(analyzer="word", ngram_range=(1,1), stop_words={'english'})
X_train_counts =count_vect.fit_transform(X_train)  
X_test_counts=count_vect.transform(X_test) 
print("X_train_counts shape:",X_train_counts.shape)
tf=TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf=tf.transform(X_train_counts)
print("X_train_tf_counts shape:",X_train_tf.shape)
X_test_tf=tf.transform(X_test_counts)
print("X_test_tf shape:",X_test_tf.shape)
print("y_train shape:", len(y_train))
print("y_test shape:",len(y_test))
clf=BernoulliNB()
clf1=MultinomialNB()
clf.fit(X_train_tf,y_train)
acc=clf.score(X_test_tf, y_test)
print(acc)
y_pred=clf.predict(X_test_tf)
count=0
for i in range(0, len(X_test)):
  if(y_pred[i]==y_test[i]):
      count+=1
accuracy=(count/len(X_test))*100
print(accuracy)     

