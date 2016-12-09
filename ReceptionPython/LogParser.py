#!/usr/bin/env python

import sys
import numpy as np
from operator import itemgetter, attrgetter
import Image
from math import *

try:
    sys.argv[1]
except NameError:
    startingpoint = 'Missing an arg'
else:
    startingpoint = sys.argv[1]

i = 0
MegaLine = []
Tableau = []
BaseData = []



print BaseData
print "\n\n"

with open(startingpoint, 'r') as echOpenLog:
	for line in echOpenLog:
		if (i==4):
			#print MegaLine
			Tableau.append(MegaLine)
			i=0
		if (i==0):
			line = line.split('\t')
			del line[0]
			del line[-1]
			MegaLine = line
		else:
			line = line.split('\t')
			del line[0]
			del line[0]
			del line[-1]
			MegaLine += line
		i=i+1

Tableau.append(MegaLine)

data = np.array(Tableau).astype(int)
col = 0

SortedTable = data[np.argsort(data[:,col])]
PointsPerLine = len(SortedTable[0])
NbOfPoints = len(SortedTable)
print PointsPerLine
print NbOfPoints


targetFile = open("debug.log", 'w')
moyenneLine =[]
FinReset = 200
moyenne = []


##On cree le fichier de debug.. et la moyenne sur les 200 derniers points
for x in range(NbOfPoints):
	for y in range (PointsPerLine):
		SortedTable[x][y] = int(SortedTable[x][y])
		targetFile.write(str(SortedTable[x][y])+"\t")
		if (y>PointsPerLine-FinReset):
			moyenneLine.append(int(SortedTable[x][y]))
	targetFile.write("\n")



##On retire le niveau sur les 200 derniers points pour moyenner

for x in range(NbOfPoints):
	TMP_Mean = sum(moyenneLine) / float(len(moyenneLine))
	for y in range (PointsPerLine):
		SortedTable[x][y] = int(abs(float(SortedTable[x][y]) - TMP_Mean))



##On retire les echos initiaux
InitReset = 190
moyenne = []
for x in range(NbOfPoints):
	for y in range (PointsPerLine):
		if (y<InitReset):
			moyenne.append(int(SortedTable[x][y]))
		else:
			moyenne.append(0)
	moyenne[y] = int(moyenne[y]/InitReset)


size = (NbOfPoints,PointsPerLine)
print size
im = Image.new('RGB',size)
pix = im.load()

for i in range(size[0]):
    for j in range(size[1]):
	value = abs((int(SortedTable[i][j]))-moyenne[j])
	SortedTable[i][j] = int(value **(1/1))

SortedTable = SortedTable[np.argsort(SortedTable[:,col])]
print SortedTable

for i in range(size[0]):
    for j in range(size[1]):
	value = int(SortedTable[i][j])
        pix[i,j] = (value,value,value) 

outfile = startingpoint +".png"
im.save(outfile)


	
