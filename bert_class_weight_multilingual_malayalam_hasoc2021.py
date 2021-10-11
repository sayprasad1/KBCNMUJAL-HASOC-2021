# -*- coding: utf-8 -*-
"""BERT-Class weight- Multilingual-GERMAN LANG MALAYALAM hasoc2021.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WmcbQu-c1_Zv9v6MGsDKbyJd_TqNlD3E
"""

from google.colab import files
uploaded = files.upload()

# install simpletransformers
!pip install simpletransformers

# check installed version
!pip freeze | grep simpletransformers

pip install tensorboardX

import pandas as pd
from simpletransformers.classification import ClassificationModel

Mal_train=pd.read_csv("Mal_sentiment_full_train.tsv" , sep='\t')
Mal_train.head()

pip install ml2en

from ml2en import ml2en

converter = ml2en()

desti_lang={
     'malayalam' : 'ml'
}

Mal_train=pd.read_csv("Mal_sentiment_full_train.tsv" , sep='\t')
Mal_Dev=pd.read_csv("Mal_sentiment_full_dev.tsv" , sep='\t')
Mal_test=pd.read_csv("Mal_sentiment_full_test_withoutlabels.tsv" , sep='\t')

for key,value in desti_lang.items():
     #print(transt.translate(Mal_train['text']))
        Mal_train['text1']=Mal_train['text'].apply(lambda x: converter.transliterate(x))
        Mal_Dev['text1']=Mal_Dev['text'].apply(lambda x: converter.transliterate(x))
        Mal_test['text1']=Mal_test['text'].apply(lambda x: converter.transliterate(x))

Mal_train.head()

Mal_train['category'].value_counts()
Mal_Dev['category'].value_counts()

msg=Mal_train['text1']

msgDev=Mal_Dev['text1']

msgTest=Mal_test['text1']

import regex
import re
import numpy as np

Mal_train.head()

#Remove Emojis

def emoji(msg): 
    
    msg_emoj=msg.str.replace(r'[(\U0001F600-\U0001F92F|\U0001F300-\U0001F5FF|\U0001F680-\U0001F6FF|\U0001F190-\U0001F1FF|\U00002702-\U000027B0|\U0001F926-\U0001FA9F|\u200d|\u2640-\u2642|\u2600-\u2B55|\u23cf|\u23e9|\u231a|\ufe0f)]+','')
    
    msg_digit=msg_emoj.str.replace(r'[0-9]', ' ')

    msg_Spac = msg_digit.str.replace(r'_',' ')

    msg_Spac = msg_Spac.str.replace(r'.','')

    msg_Spac = msg_Spac.str.replace(r'!','')

    msg_Spac = msg_Spac.str.replace(r'#','')

    msg_Spac = msg_Spac.str.replace(r'%','')

    msg_Spac = msg_Spac.str.replace(r'&','')

    msg_Spac = msg_Spac.str.replace(r'’','')

    msg_Spac = msg_Spac.str.replace(r'(','')

    msg_Spac = msg_Spac.str.replace(r')','')

    msg_Spac = msg_Spac.str.replace(r'-','')

    msg_Spac = msg_Spac.str.replace(r'/','')

    msg_Spac = msg_Spac.str.replace(r':','')

    msg_Spac = msg_Spac.str.replace(r';','')

    msg_Spac = msg_Spac.str.replace(r'<','')

    msg_Spac = msg_Spac.str.replace(r'=','')

    msg_Spac = msg_Spac.str.replace(r'>','')

    msg_Spac = msg_Spac.str.replace(r'?','')

    msg_Spac = msg_Spac.str.replace(r'@','')

    msg_Spac = msg_Spac.str.replace(r'[','')

    msg_Spac = msg_Spac.str.replace(r']','')

    msg_Spac = msg_Spac.str.replace(r'^','')

    msg_Spac = msg_Spac.str.replace(r'{','')

    msg_Spac = msg_Spac.str.replace(r'}','')

    msg_Spac = msg_Spac.str.replace(r'|','')

    msg_Spac = msg_Spac.str.replace(r'~','')

    msg_Spac = msg_Spac.str.replace(r'+','')

    msg_Spac = msg_Spac.str.replace(r'\s+', ' ')


    return msg_Spac

msg_Train=emoji(msg)

msg_Dev=emoji(msgDev)

msg_Test=emoji(msgTest)

Train_Df=pd.DataFrame(msg_Train)
Train_Df.columns=['Msg_with_Stopwords']

Dev_Df=pd.DataFrame(msg_Dev)
Dev_Df.columns=['Msg_with_Stopwords']

Test_Df=pd.DataFrame(msg_Test)
Test_Df.columns=['Msg_with_Stopwords']

Train_Df.shape, Dev_Df.shape, Test_Df.shape

# Removing Null Values

Train_Df['Msg_with_Stopwords']=Train_Df['Msg_with_Stopwords'].fillna("")

Dev_Df['Msg_with_Stopwords']=Dev_Df['Msg_with_Stopwords'].fillna("")

Test_Df['Msg_with_Stopwords']=Test_Df['Msg_with_Stopwords'].fillna("")

Mal_train.shape, Mal_Dev.shape,Train_Df.shape, Dev_Df.shape, Mal_test.shape, Test_Df.shape#

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

Train_Df['Msg_without_Stopwords']=Train_Df['Msg_with_Stopwords'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

Dev_Df['Msg_without_Stopwords']=Dev_Df['Msg_with_Stopwords'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

Test_Df['Msg_without_Stopwords']=Test_Df['Msg_with_Stopwords'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

Train_Df['Msg_with_Stopwords_Len'] = [len(x.split()) for x in Train_Df['Msg_with_Stopwords'].tolist()]
Train_Df['Msg_without_Stopwords_Len'] = [len(x.split()) for x in Train_Df['Msg_without_Stopwords'].tolist()]

Dev_Df['Msg_with_Stopwords_Len'] = [len(x.split()) for x in Dev_Df['Msg_with_Stopwords'].tolist()]
Dev_Df['Msg_without_Stopwords_Len'] = [len(x.split()) for x in Dev_Df['Msg_without_Stopwords'].tolist()]

Test_Df['Msg_with_Stopwords_Len'] = [len(x.split()) for x in Test_Df['Msg_with_Stopwords'].tolist()]
Test_Df['Msg_without_Stopwords_Len'] = [len(x.split()) for x in Test_Df['Msg_without_Stopwords'].tolist()]

Train_Data=pd.concat([Mal_train, Train_Df], axis=1)

Dev_Data=pd.concat([Mal_Dev, Dev_Df], axis=1)

Test_Data=pd.concat([Mal_test, Test_Df], axis=1)

Train_Data.shape, Dev_Data.shape, Test_Data.shape

Train_Data=Train_Data.drop(['Msg_with_Stopwords','Msg_without_Stopwords_Len', 'Msg_with_Stopwords_Len', 'text'], axis=1)

Dev_Data=Dev_Data.drop(['Msg_with_Stopwords','Msg_without_Stopwords_Len', 'Msg_with_Stopwords_Len', 'text'], axis=1)

Test_Data=Test_Data.drop(['Msg_with_Stopwords','Msg_without_Stopwords_Len', 'Msg_with_Stopwords_Len', 'text'], axis=1)

Train_Data.shape, Dev_Data.shape, Test_Data.shape

Train_Data.head()

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

Train_Data['Nlabel']=le.fit_transform(Train_Data['category']) 
Dev_Data['Nlabel']=le.fit_transform(Dev_Data['category'])

Train_Data.head()

Train_Data=Train_Data.drop(['text1','category'], axis=1)

Dev_Data=Dev_Data.drop(['text1','category'], axis=1)

Test_Data=Test_Data.drop(['text1'], axis=1)

Train_Data.head()

Dev_Data.head()

Test_Data.head(2)

from sklearn.utils import class_weight

class_weights = class_weight.compute_class_weight('balanced',
                                                 np.unique(Train_Data.Nlabel),
                                                 Train_Data.Nlabel)
class_weights

from simpletransformers.classification import ClassificationArgs

import torch
cuda_available = torch.cuda.is_available()
cuda_available

# define hyperparameter
model_args ={"reprocess_input_data": True,
             "fp16":False,
             "num_train_epochs": 4,
             "overwrite_output_dir" : True}

# Create a ClassificationModel
model = ClassificationModel(
    "bert", "bert-base-multilingual-cased",
    num_labels=5,
    weight=[3.43153348, 1.50954869, 0.49487619, 2.74641314, 0.60193218],
    use_cuda=cuda_available,
    args=model_args
)

model.train_model(Train_Data)

from sklearn.metrics import f1_score, accuracy_score


def f1_multiclass(labels, preds):
    return f1_score(labels, preds, average='micro')
    
result, model_outputs, wrong_predictions = model.eval_model(Dev_Data, f1=f1_multiclass, acc=accuracy_score)

result

prediction=model.predict(Dev_Data['Msg_without_Stopwords'].values.tolist())

prediction=prediction[0]
prediction

type(prediction), prediction.shape

import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import precision_score, recall_score, f1_score

X_dev1=Dev_Data['Msg_without_Stopwords']
y_dev1=Dev_Data['Nlabel']

print(classification_report(y_dev1, prediction))

