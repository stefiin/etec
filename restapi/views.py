from django.shortcuts import render

# Create your views here.

'''import requests
import json
import matplotlib.pyplot as plt
import collections
from collections import Counter
from sortedcontainers import SortedList, SortedSet, SortedDict

workingData={}
workingVolume={}

#Creates initial file
def createFile():
    #define API Call on file creation
    API_URL = "https://www.alphavantage.co/query"
    data = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": "ACB.TO",
        "interval": "1min",
        "outputsize": "full",
        "apikey": "3RCK5SVL7J3XAPKL",
    }
    #get response from API
    response = requests.get(API_URL, data)

    #create the file with initial data
    with open('ACB.json', 'w') as outfile:
        json.dump(response.json(), outfile, sort_keys = True, indent = 4, ensure_ascii = False)

def addData():
    
    API_URL = "https://www.alphavantage.co/query"
    data = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": "ACB.TO",
        "interval": "1min",
        "outputsize": "compact",
        "apikey": "3RCK5SVL7J3XAPKL",
    }
    response = requests.get(API_URL, data)

    with open('tempACB.json', 'w') as newData:
        json.dump(response.json(), newData, sort_keys = True, indent = 4, ensure_ascii = False)
    
    trigger=0

    with open('ACB.json',) as f, open('tempACB.json') as t:
        datas = json.load(f)
        temp = json.load(t)

    tempData=(temp['Time Series (1min)'])
    fullData=(datas['Time Series (1min)'])
    lastValue=list(fullData.keys())[-1]
    
    #parse full data so it only returns last 10 days
    if len(fullData)>10:
        for key in fullData.keys():
                 
    #Find the last value of the full data and add the temp data to it
    for key in tempData.keys():
        if key==lastValue:
            trigger=1
            continue
        if trigger==1:
            fullData[key]=tempData[key]
    
    with open('ACBDynamic.json', 'w') as out:
        json.dump(fullData, out, sort_keys = True, indent = 4, ensure_ascii = False)

def getStats():
    with open('ACBDynamic.json') as f:
        data = json.load(f)

    for priceKey in data.keys():
        lowMap=(data[priceKey])
        lowPrice=lowMap['3. low']
        lowVolume=lowMap['5. volume']        
        #this is the raw data that holds the low price
        workingData[priceKey]=float(lowPrice)
        #this is the raw data that holds the volume
        workingVolume[priceKey]=float(lowVolume)
    #this gets the unique prices in the raw data
    bins=SortedSet(workingData.values())
    totalVolume=0
    magic={}
    #iterate through each unique price
    for b in bins:
        binVolume=0      
        #iterate through the raw price data
        for key in workingData.keys():
            #if the bin is equal to the raw data price, add the volume to the bin
            if workingData[key]==b:
                currentVolume=workingVolume[key]
                binVolume=binVolume+currentVolume
                totalVolume=totalVolume+currentVolume
        #this dictionary holds the magic
        magic[b]=binVolume
      
    previousBin=0 
    CDF={}
    #build the CDF
    for key in magic.keys():
        CDF[key]=magic[key]/totalVolume+previousBin
        previousBin=CDF[key]
    #build the PDF
    PDF={}
    for key in magic.keys(): 
        PDF[key]=magic[key]/totalVolume
    #get highest volume prices
    
    sorted_by_value = sorted(PDF.items(), key=lambda kv: kv[1])
    print(sorted_by_value)
    #prints lowest volumes
    print(sorted_by_value[0:5])
    #prints highest volumes 
    print(sorted_by_value[-5:-1],sorted_by_value[-1])
    
    
    price=list(CDF.keys())
    volume=list(CDF.values())
    plt.plot(price, volume, '*')
    plt.xticks(fontsize=10, rotation=90)
    plt.show()

import json
import matplotlib.pyplot as plt
import collections
from sortedcontainers import SortedList, SortedSet, SortedDict

totalVolume=0
previousBin=0

workingData={}
workingVolume={}
distribution={}

with open('ACBDynamic.json') as f:
    data = json.load(f)

for priceKey in data.keys():
    lowMap=(data[priceKey])
    lowPrice=lowMap['3. low']
    lowVolume=lowMap['5. volume']
    workingData[priceKey]=float(lowPrice)
    workingVolume[priceKey]=float(lowVolume)

bins=SortedSet(workingData.values())
for b in bins:
    binVolume=0
    for key in workingData.keys():
        if workingData[key]==b:
            currentVolume=workingVolume[key]
            binVolume=binVolume+currentVolume
            totalVolume=totalVolume+currentVolume
    distribution[b]=binVolume
sortedDist=SortedDict(distribution)

for key in sortedDist.keys():
    sortedDist[key]=sortedDist[key]/totalVolume+previousBin
    previousBin=sortedDist[key]
    
price=list(sortedDist.keys())
volume=list(sortedDist.values())
plt.plot(price, volume, '*')
plt.xticks(fontsize=10, rotation=90)
plt.show()

#print(workingVolume)
#print(workingData)


#createFile()
addData()
#getStats()'''