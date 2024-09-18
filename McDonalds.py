import csv
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def Graph():
    with open(r"McDonalds.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        df = pd.DataFrame([csv_reader], index=None)
        df.head()

    guestCountTotal = []
    dates = []
    total = 0
    date = list(df[1])[0][0]
    for row in range(1, 5959):
        for val in list(df[row]):
            if date != val[0]:
                dates.append(date)
                guestCountTotal.append(total)
                date = val[0]
                total = 0
            total += int(val[6])

    #dates.append()
    #guestCountTotal.append(total)

    x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
    y = np.array(guestCountTotal)

    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b/%Y'))


    plt.scatter(x, y)
    plt.gcf().autofmt_xdate()
    plt.show()

