# Author: Julien Dambrine, Poitiers University
# Please if you use this code the references to mention are:
# CHASSAGNE R, OBIDEGWU D, DAMBRINE J, MACBETH C. 
# Binary 4D Seismic History Matching, a Metric Study. 
# Computers & Geosciences, 96, 159-172, 2016.
# and
# Glaunès, J., Qiu, A., Miller, M.I., Younes, L., 2008. 
# Large deformation diffeomorphic metric curve mapping. 
# Int. J. Comput. Vis. 80 (3), 317–336.

import numpy
import math
def currentDistSobolev(A,B,p):
	dims=A.shape
	Nx=dims[0]
	Ny=dims[1]
	Kernel=numpy.zeros((Nx,Ny))
	for j in range(Ny):
		for i in range(Nx):
			if(i<=Nx/2):
				kx=i
			else:
				kx=Nx-i

			if(i<=Ny/2):
				ky=j
			else:
				ky=Ny-j

			k=math.sqrt(kx*kx+ky*ky)

	Kernel[i,j]=(k**2)/((1.0+k)**p)
	D_FT=numpy.fft.fft2(A-B)
	KD_FT=D_FT*Kernel

	return abs(numpy.vdot(numpy.reshape(D_FT,[1,Nx*Ny]),numpy.reshape(KD_FT,[Nx*Ny,1])))



