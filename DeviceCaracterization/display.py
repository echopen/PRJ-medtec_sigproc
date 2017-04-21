'''
Lets study the two raw images we have : one of a plate and one of a hand
''' 

import numpy as np
import matplotlib.pyplot as plt
plt.clf()

Nsample = 1689 # number of samples by line
Nline = 64 # number of lines

#%% The plate

'''
Let mesure the SNR and have a look at the data. for computing the SNR,
I compute the variance one the empty half side of the image. This will be my
estimate of the noise power. To compute the power of the signal, i mesure the
highest possible amplitude and square it.
'''

# image plotting

plate = np.loadtxt('plate.txt')
plt.figure(1)
plt.title('plate raw image')
plt.imshow(abs(sp.hilbert(plate)), cmap='gray', aspect='auto')
plt.colorbar()
plt.xlabel('samples')
plt.ylabel('lines')

Nempty = 32 # separe the empty from the not empty side
Nplot = 46 # one line chosen for graph display

# repere plotting

plt.plot([0,Nsample-1],[Nempty-0.5,Nempty-0.5],'b--',label='empty line')
plt.plot([0,Nsample-1],[Nplot,Nplot],'r--',label='plot line')
plt.legend()

# graph plotting

plt.figure(2)
plt.title('one line plotting')
plt.plot(abs(sp.hilbert(plate[Nplot,:])),'r')
plt.xlabel('samples')
plt.ylabel('amplitude')

# SNR computation

Pnoise = np.var(plate[:Nempty,:])
Psignal = ((np.max(plate) - np.min(plate))/2)**2
print('SNR :', '{:.1f}'.format(10*np.log10(Psignal/Pnoise)),'dB')

#%% The hand

#plot it for fun

hand = np.loadtxt('hand.txt')
plt.figure(3)
plt.title('hand raw image')
plt.imshow(abs(sp.hilbert(hand)), cmap='gray', aspect='auto')
plt.colorbar()
plt.xlabel('samples')
plt.ylabel('lines')
