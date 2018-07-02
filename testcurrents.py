# Author: Julien Dambrine, Poitiers University
# Please if you use this code the references to mention are:
# CHASSAGNE R, OBIDEGWU D, DAMBRINE J, MACBETH C. 
# Binary 4D Seismic History Matching, a Metric Study. 
# Computers & Geosciences, 96, 159-172, 2016.
# and
# Glaunès, J., Qiu, A., Miller, M.I., Younes, L., 2008. 
# Large deformation diffeomorphic metric curve mapping. 
# Int. J. Comput. Vis. 80 (3), 317–336.

import currents
import numpy

A=numpy.zeros((8,8))
B=numpy.zeros((8,8))

for i in range(8):
	for j in range(8):
		if(abs(i-4)<2 and abs(j-4)<2):
			B[i,j]=1
		if(abs(i-6)<2 and abs(j-6)<2):
			A[i,j]=1
print ('A = ')
print (A)
print ('B = ')
print (B)
print ('Current Distance :')
print (currents.currentDistSobolev(A,B,2))
