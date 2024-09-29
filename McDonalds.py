import csv
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from collections import OrderedDict

def Graph(day = None, time = None):
    df = pd.read_csv('McDonalds.csv')

    data = dict()
    dateList = list(df["Date"])
    #dates = list(OrderedDict.fromkeys(dateList))

    DTGCList = df["DT GC"]

    if (day == None and time == None):
        filterList = [ range(0, len(DTGCList)) ]
   
    elif (day == None):
        filterList = df.loc[ (df['Time Slice'] == '4am-11am') ].index.tolist()
    
    elif (time == None):
        filterList = df.loc[ (df['Time Slice'] == '4am-11am')  ].index.tolist()

    else:
        filterList = df.loc[ (df['Time Slice'] == '4am-11am') & (df["Weekday"] == "Sunday") ].index.tolist()

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
    df = pd.read_csv('McDonalds.csv')

    data = dict()
    dateList = df["Date"]
    dates = list(OrderedDict.fromkeys(dateList))
    for date in dates:
        data[date] = 0

    DTGCList = df["DT GC"]

    for i in range(0, len(DTGCList)):
        data[dateList[i]] += DTGCList[i]

    x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
    y = data.values()
    print(dateList[0]) 
    #print(df.loc[df['Time Slice'] == '4am-11am'].index.tolist())
    #print(df[df['Time Slice'] == '4am-11am'])