import csv
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def Graph():
    df = pd.read_csv('McDonalds.csv')

    data = dict()
    dateList = df["Date"]
    dates = list(set(dateList))
    for date in dates:
        data[date] = 0

    DTGCList = df["DT GC"]

    for i in range(0, len(DTGCList)):
        data[dateList[i]] += DTGCList[i]

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
    dates = list(set(dateList))
    for date in dates:
        data[date] = 0

    DTGCList = df["DT GC"]

    for i in range(0, len(DTGCList)):
        data[dateList[i]] += DTGCList[i]
    
    x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in data.keys()]
    y = np.array(data.values())
    print(len(dates))
    print(len(x))
    print(len(data.values()))
