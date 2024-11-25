import csv
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from collections import OrderedDict

def Graph(day, time):
    df = pd.read_csv('McDonaldsTest.csv')

    data = dict()
    dateList = df["Date"]
    dates = []
    filterList = []
    #dates = list(OrderedDict.fromkeys(dateList))

    DTGCList = df["DT GC"]

    if (day == 'Everyday' and time == 'Whole Day'):
        filterList = list(range(0, len(DTGCList)))
        print(1)
   
    elif (time == "Whole Day"):
        filterList = df.loc[ (df['Weekday'] == day) ].index.tolist()
        print(2)
    elif (day == "Everyday"):
        filterList = df.loc[ (df['Time Slice'] == time)  ].index.tolist()
        print(3)
    else:
        filterList = df.loc[ (df['Time Slice'] == time) & (df["Weekday"] == day) ].index.tolist()
        print(4)

    for i in filterList:
        data[ dateList[i] ] = 0
    
    for i in filterList:
        data[ dateList[i] ] += DTGCList[i]

    x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in data.keys()]
    y = data.values()
    
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b/%Y'))

    plt.scatter(x, y)
    plt.gcf().autofmt_xdate()
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('McDonaldsTest.csv')
    day = None
    time = None
    data = dict()
    dateList = df["Date"]
    dates = []
    filterList = []
    #dates = list(OrderedDict.fromkeys(dateList))

    DTGCList = df["DT GC"]

    if (day == None and time == None):
        filterList = list(range(0, len(DTGCList)))
   
    elif (day == None):
        filterList = df.loc[ (df['Time Slice'] == '4am-11am') ].index.tolist()
    
    elif (time == None):
        filterList = df.loc[ (df['Time Slice'] == '4am-11am')  ].index.tolist()

    else:
        filterList = df.loc[ (df['Time Slice'] == '4am-11am') & (df["Weekday"] == "Sunday") ].index.tolist()

    #print(filterList)
    for i in filterList:
        data[ dateList[i] ] = 0
    
    for i in filterList:
        data[ dateList[i] ] += DTGCList[i]
        #print(DTGCList[i])

    x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in data.keys()]
    y = data.values()
    
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b/%Y'))

    plt.scatter(x, y)
    plt.gcf().autofmt_xdate()
    plt.show()