import csv
import datetime
#import numpy as np
#import pylab

#explicitly force TkAgg as backend
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#explicitly force TkAgg as backend

with open('telemetry.csv') as csvfile:
    #readCSV = csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
    readCSV = csv.reader(csvfile, delimiter=',')
    times = []
    points = []
    altitudes = []
    powers = []
    freqs = []
    timesstrp = []


    for row in readCSV:
        time = row[3]
        point = row[0]
        altitude = row[6]
        power = row[13]

        points.append(point)
        times.append(time)
        altitudes.append(altitude)
        powers.append(power)

    #timesstrp = [datetime.datetime.strptime(times, '%H:%M:%S') for times in timesstrp]


    del points[:5]
    del times[:5]
    del altitudes[:5]
    del powers[:5]

    print(times)
    print(points)
    print(altitudes)
    print(powers)
   #print(freqs)
   #print(timesstrp)

    backend = plt.get_backend()
    print backend


    times = [datetime.datetime.strptime(elem, '%H:%M.%S') for elem in times]
    print times
    #y = [1,10]


    #plt.plot(powers, linewidth=2.0)
    #plt.plot(altitudes)
    #plt.show()

    (fig, ax) = plt.subplots(1, 1)
    ax.plot(times, altitudes)
    plt.show()              #this is the fix change fig.show() to plt.show()