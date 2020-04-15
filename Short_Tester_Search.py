 # -*- coding: UTF-8 -*-

from datetime import date
import os.path
import time
import re
import shutil
import pandas as pd
import selenium
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
import xlsxwriter
import datetime
from datetime import datetime
import os
import glob
import pywinauto
from pywinauto.application import Application

from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import pandas as pd 
import pickle
import numpy as np
import pandas as pd
import sklearn.model_selection as ms
import datetime
from datetime import date
from datetime import datetime
import re
from sklearn import ensemble
from sklearn.metrics import recall_score
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV
randomForest = ensemble.RandomForestClassifier(n_jobs=5, verbose=3)
import numpy as np
import pickle
import xlsxwriter
from PyDictionary import PyDictionary
import nltk
nltk.download('words')
dictionary=PyDictionary()
from nltk.corpus import words

word_list = words.words()


starttime = datetime.now()


def check_exists_by_xpath(xpath):
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        print("Could not find Update Button.")
        return False
    return True


week_days= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
weeknum =[0,1,2,3,4,5,6,7]

weekdaydict = dict(zip(weeknum,week_days))

shortweeknum=[0,1,2,3,4,5]
period_length=[3,5,1,2,1,1]

tester_period_dict=dict(zip(shortweeknum, period_length))


todaysdate = datetime.now()
todaystr=str(todaysdate)

date_N_days_ago = datetime.now() - timedelta(days=tester_period_dict[todaysdate.weekday()])

print("date_N_days_ago", date_N_days_ago)

print("fromDate", date_N_days_ago)


fromweekday = date_N_days_ago.weekday()

fromdate = str(date_N_days_ago)
fromMonth = fromdate[5:7]
fromDay = fromdate[8:10]
fromYear = fromdate[:4]

toMonth = todaystr[5:7]
toDay = todaystr[8:10]
toYear = todaystr[2:4]

fromHH = "00"
fromMM = "00"

toHH = "00"
toMM = "00"

print(fromMonth)
print(fromDay)
print(fromYear)

print(toMonth)
print(toDay)
print(toYear)

monthdict=dict(zip(['01','02','03','04','05','06','07','08','09','10','11','12'],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']))

fromMonth = str(monthdict[fromMonth])

todayshort = str(weekdaydict[fromweekday])
todayshort = todayshort[:3]
fromDaystr = str(fromDay)

fromDaystrlong = "'" +  todayshort + " " + fromMonth + " " + fromDaystr + " " + fromYear + "'"

print(fromDaystrlong)

####Identifying Testers


#####For Training

#latesttrainingset
# df=pd.read_csv("C:\\Users\\f6b1tf6\\Documents\\fulltrainingset0309.csv")
# df=df[0:200000]

# print("df", df.head())
# testy = df.iloc[:,2:3]
# print(type(testy))
# print("testy", testy.head())

# os.chdir("C:/Users/f6b1tf6/Downloads")
# files = glob.glob("*.csv")
# files.sort(key=os.path.getmtime)
# shortfiles = files[-1:]
# todaysfile=str(shortfiles[0])
# print(todaysfile)


_0df=pd.read_csv("C:\\Users\\f6b1tf6\\Documents\\icul_investigation.csv")

df=_0df.rename(columns={"merchant_name": "Name"})

# df=_0df[~_0df['Name'].str.contains('\s+INC$|\s+ORG$|\s+COM$', na=False)]


###filtering out known non-gibberish rows to reduce number of rows

print(df.head())

double = ['AA',
'BB',
'CC',
'DD',
'EE',
'FF',
'GG',
'HH',
'II',
'JJ',
'KK',
'LL',
'MM',
'NN',
'OO',
'PP',
'QQ',
'RR',
'SS',
'TT',
'UU',
'VV',
'WW',
'XX',
'YY',
'ZZ']

bigrams = ['BK',
'BQ',
'BX',
'CB',
'CF',
'CG',
'CJ',
'CP',
'CV',
'CW',
'CX',
'DX',
'FK',
'FQ',
'FV',
'FX',
'FZ',
'GQ',
'GV',
'GX',
'HK',
'HV',
'HX',
'HZ',
'IY',
'JB',
'JC',
'JD',
'JF',
'JG',
'JH',
'JK',
'JL',
'JM',
'JN',
'JP',
'JQ',
'JR',
'JS',
'JT',
'JV',
'JW',
'JX',
'JY',
'JZ',
'KQ',
'KV',
'KX',
'KZ',
'LQ',
'LX',
'MG',
'MJ',
'MQ',
'MX',
'MZ',
'PQ',
'PV',
'PX',
'QB',
'QC',
'QD',
'QE',
'QF',
'QG',
'QH',
'QJ',
'QK',
'QL',
'QM',
'QN',
'QO',
'QP',
'QR',
'QS',
'QT',
'QV',
'QW',
'QX',
'QY',
'QZ',
'SX',
'SZ',
'TQ',
'TX',
'VB',
'VC',
'VD',
'VF',
'VG',
'VH',
'VJ',
'VK',
'VM',
'VN',
'VP',
'VQ',
'VT',
'VW',
'VX',
'VZ',
'WQ',
'WV',
'WX',
'WZ',
'XB',
'XG',
'XJ',
'XK',
'XV',
'XZ',
'YQ',
'YV',
'YZ',
'ZB',
'ZC',
'ZG',
'ZH',
'ZJ',
'ZN',
'ZQ',
'ZR',
'ZS',
'ZX']


namelist = list(df['Name'])

dictionary_list=[]
allcapslist=[]
# numberofspaceslist = []
lettersinarowlist = []
containsbigramslist= []
alphalist = []

for i in namelist:
    name = str(i)
    if name.isupper() == True:
        allcapslist.append("1")
    else:
        allcapslist.append("0")
    # b = name.count(' ')
    # numberofspaceslist.append(b)
    f = name.replace(' ', '')
    if f.isalpha():
        alphalist.append("1")
    else:
        alphalist.append("0")

def createbigrams(str):
    wordlist = list(str)
    listlen=len(wordlist)
    listlenshort = listlen-1
    strbigramlist=[]
    for i in range(0,listlenshort):
        first = wordlist[i]
        next = i + 1
        new = first + wordlist[next]
        strbigramlist.append(new)
    shortestbigram = set(strbigramlist)
    sett = shortestbigram.intersection(bigrams)
    if len(sett) == 0:
        containsbigramslist.append("0")
    else:
        containsbigramslist.append("1")

containsdoublebigramslist = []

def createdoublebigrams(str):
    wordlist = list(str)
    listlen=len(wordlist)
    listlenshort = listlen-1
    strbigramlist=[]
    for i in range(0,listlenshort):
        first = wordlist[i]
        next = i + 1
        new = first + wordlist[next]
        strbigramlist.append(new)
    shortestbigram = set(strbigramlist)
    sett = shortestbigram.intersection(bigrams)
    if len(sett) < 2:
        containsdoublebigramslist.append("0")
    else:
        containsdoublebigramslist.append("1")
 

def createdoubles(input):
    input=str(input)
    listlenshort=len(input) - 2
    strbigramlist=[]
    for i in range(0,listlenshort):
        next = i+2
        pair=input[i:next]
        strbigramlist.append(pair)
    shortestbigram = set(strbigramlist)
    sett = shortestbigram.intersection(double)
    if len(sett) == "0":
        lettersinarowlist.append("0")
    else:
        lettersinarowlist.append("1")

print("creating bigrams")
print("createdoublebigrams")
print("create doubles")


for i in namelist:
    m = str(i)
    createbigrams(m)
    createdoubles(m)
    createdoublebigrams(m)


print("extracting COM information")
comlist = []
for i in namelist:
    m = str(i)
    if "COM" in m:
        comlist.append("1")
    else:
        comlist.append("0")

vowels = ['a', 'e', 'i', 'o', 'u']
vowelset=set(vowels)

print("Extracting Vowel Info")
vowellist=[]
for i in namelist:
    m = str(i)
    mlist = set(list(m.lower()))
    newvowelset = mlist.intersection(vowelset)
    u = len(newvowelset)
    vowellist.append(u)

print("Adding Lists")

testx=pd.DataFrame()
# testx['Number of Spaces'] = numberofspaceslist
testx['All Uppercase'] = allcapslist
testx['Contains Bigrams'] = containsbigramslist
testx['Contains Letters in a Row'] = lettersinarowlist
testx['Contains Non-Letters'] = alphalist
testx['Contains Double Bigrams'] = containsdoublebigramslist
testx['Contains Com'] = comlist
testx['Vowels'] = vowellist


print(testx.columns)

dayy = date.today().strftime('%d_%m_%Y')

##
##
##
###Training the Model 

# testx_train, testx_test, testy_train, testy_test = ms.train_test_split(
#     testx, testy, test_size=1/2, random_state=0
# )


# scorer=make_scorer(recall_score, average='micro')

# randomForest.fit(testx_train, testy_train)

# foresttrainpred=randomForest.predict(testx_train)
# foresttestpred=randomForest.predict(testx_test)

# trainprscore=recall_score(testy_train,foresttrainpred, average='micro')
# testprscore=recall_score(testy_test,foresttestpred, average='micro')

# print("The training error of random forest is: %.5f" %(1 - trainprscore))
# print("The test error of random forest is: %.5f" %(1 - testprscore))
# print("Random Forest Recall Score:", testprscore)


# filename = "rfmodel_" + str(testprscore) + "_" + dayy 
# pickle.dump(randomForest, open(filename, 'wb'))


# sleep(30)


##
##
##Using the Model to Identify Gibberish MIDs

##old model rfmdel0309 .99989
# filename = "rfmodel0309_nocommon_expanded0.999893188374699.sav"

# filename = "rfmodel_0.9999875_04_04_2020"


filename = "C:\\Users\\f6b1tf6\\Desktop\\Tester_Search\\rfmodel_0.9995326991393081_14_04_2020_latest_nospace"
print("Loading Model")

lmodel = pickle.load(open(filename, 'rb')) 



print("Predicting Results")
testypred = lmodel.predict(testx)

testypred.reshape(-1,1)
preddf = pd.DataFrame(testypred)
caiddf = pd.DataFrame(df['card_acceptor_id'])
merchantnamedf = pd.DataFrame(df['Name'])
# carddf = pd.DataFrame(df['card_number'])




print("Generating Final Results DataFrame")
preddf= pd.concat([preddf, merchantnamedf, caiddf], axis=1)

preddf=preddf.rename(columns={0:"Output"})
print(preddf)


print("Exporting Testers to Excel")

filenametest = dayy + "_Gibberish_Tester_Results_Testers.xlsx"
writer=pd.ExcelWriter(filenametest, engine = 'xlsxwriter')
preddf['Output Str'] = preddf['Output'].astype(str)
testdf = preddf[preddf['Output Str'].str.contains('1')]

##getting the longest length between spaces

##dictionary stuff


first_lenlist = []
for i in testdf['Name']:
    m = str(i)
    mlist = m.split()
    first_lenlist.append(mlist)

second_lenlist = []
for i in first_lenlist:
    second_lenlist.extend(i)

third_lenlist = []
for i in second_lenlist:
    third_lenlist.append(len(i))


word_list = [word for word in word_list if len(word) > 3]

max_length_between_spaces = max(third_lenlist)+1

word_list = [word for word in word_list if len(word) < max_length_between_spaces]


def check_dict(input):
    for key in word_list:
        strkey=str(key)
        if strkey in input.lower():
            dictionary_list.append(input)
            break
        else:
            continue

for i in testdf['Name']:
    m=str(i)
    check_dict(m)

new_dictionary_list=[]
for i in testdf['Name']:
    if i in dictionary_list:
        new_dictionary_list.append("1")
    else:
        new_dictionary_list.append("0")


testdf['dictionary']=new_dictionary_list

testdf['dictionary']=testdf['dictionary'].astype(str)

testdf=testdf[~testdf['dictionary'].str.contains('1')]


testdf.to_excel(writer)


writer.close()
writer.save()

filename = dayy + "_Gibberish_Tester_Results.csv"
print ("Exporting Results to csv")
preddf.to_csv(filename)



# Print the feature ranking
print("Feature ranking:")


importances = list(lmodel.feature_importances_)
feature_list = list(testx.columns)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 5)) for feature, importance in zip(feature_list, importances)]


print(feature_importances)

endtime = datetime.now()
print("Total Search and Identification Process Takes: ", endtime-starttime)



