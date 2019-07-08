# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:29:42 2019

@author: acer
"""
import pylab
pylab.rcParams['lines.linewidth'] = 3
pylab.rcParams['axes.titlesize'] = 10
pylab.rcParams['axes.labelsize'] = 10
pylab.rcParams['xtick.labelsize'] = 16
pylab.rcParams['ytick.labelsize'] = 8
pylab.rcParams['xtick.major.size'] = 8
pylab.rcParams['ytick.major.size'] = 8
pylab.rcParams['legend.numpoints'] = 1
def getData(fileName):
    dataFile = open(fileName, 'r')
    xs = []
    ys = []
    dataFile.readline
    for l in dataFile:
        x, y = l.split()
        xs.append(x)
        ys.append(float(y))
    dataFile.close
#    print (xs, ys)
    return (xs, ys) 
def labelPlot():
    pylab.title('Running time of Marvel movies')
    pylab.xlabel('Marvel movies in chronological order')
    pylab.ylabel('Run time')
def plotData(fileName):
    xVals, yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    pylab.plot(xVals, yVals, 'b', label = 'Measured displacements')
    labelPlot()
def increase(fileName):
    xVals, yVals = getData(fileName)
    leno = []
    for i in range(1, len(xVals)):
           leng = yVals[i] - yVals[i - 1]
           leno.append(leng)
    return leno
print(increase('movie.txt'))
plotData('movie.txt')

    