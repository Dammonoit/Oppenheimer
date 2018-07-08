'''
Created By :- 
	Dharmendra Choudhary
	VIT university,Vellore,Tamil Nadu,India
'''

import os
import glob
import json
import unicodedata
import csv
from itertools import izip
#import pandas as pd
tweets=list()
tweets_txt=list()
tweets_userprofile_description=list()
tweets_userprofile_id=list()
for tweet in open('Outputs_txt/tweets.txt','r'):
	tweets.append(json.loads(tweet))
	
print(tweets)
print('#'*80)
for i in range(0,len(tweets)):                    
	t=tweets[i]['text']           
	t1=unicodedata.normalize('NFKD', t).encode('ascii','ignore')
	tweets_txt.append(t1)
    
print(tweets_txt[:4])
print(type(tweets_txt[0]))


for i in range(0,len(tweets)):                    
	t=tweets[i]['user']['description']           
	#t1=unicodedata.normalize('NFKD', t).encode('ascii','ignore')
	tweets_userprofile_description.append(t)

print('#'*30)
print(tweets_userprofile_description[:4])
print(type(tweets_userprofile_description[0]))

for i in range(0,len(tweets)):                    
	t=tweets[i]['user']['id']           
	#t1=unicodedata.normalize('NFKD', t).encode('ascii','ignore')
	tweets_userprofile_id.append(t)
print('#'*30)
print(tweets_userprofile_id[:4])
print(type(tweets_userprofile_id[0]))


files = glob.glob('/home/dammonoit/Desktop/twitter_app/App3/Outputs_csv/*')
for f in files:
	os.remove(f)
columnTitleRow = "ID, Tweets, Profile_Description.\n"
with open('Outputs_csv/Output.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(columnTitleRow)
with open('Outputs_csv/Output.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(izip(tweets_userprofile_id,tweets_txt))
