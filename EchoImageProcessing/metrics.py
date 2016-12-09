__author__ = 'soobash'

import os,sys
from skimage import io
from skimage import measure
import numpy as np

### define functions ######################

# incomplete, have to be written in full
def universal_quality_index(P,Q):

    block_size = 8

    P = int (P)
    Q = int (Q)

    N = block_size**2
    s= (N,N)
    sum2_filter = np.ones(s)

    im1_sq = np.dot (P,P)
    im2_sq = np.dot (Q,Q)
    im1 = np.dot (P,Q)

############################################
# average difference
def average_difference(P,Q):

    [m,n] = P.shape
    R = P-Q
    AD = ( R.sum()) / ((m)*(n))
    return (AD)
#############################################
# maximum difference
def maximum_difference(P,Q):

    [m,n] = P.shape
    R = P-Q
    MD = max(abs(R.flatten()))
    return (MD)
#############################################
# dot product

def dot_product(A,B):

    [m,n] = A.shape
    C =np.zeros([m,n])

    for i in range (0,m):
        for j in range(0,n):
            Ak = int (A[i,j])
            Bk = int (B[i,j])
            C[i,j] = Ak * Bk

    return (C)

#############################################
# structural content
def structural_content(A,B):

    B_squared = dot_product (B,B)
    Bs = B_squared.sum()

    if (Bs == 0):
        SC = Inf
    else:
        A_squared = dot_product (A,A)
        Pk = A_squared.sum()
        SC = Pk / Bs

    return (SC)
############################################
# Normalised cross-correlation
def normalised_cross_correlation(A,B):
    AB = dot_product(A,B)
    ABs = AB.sum()
    A_squared = dot_product (A,A)
    Pk = A_squared.sum()
    NK = ABs / Pk
    return (NK)

############################################
 # minkowski distance
def minkowski_distance(P,Q):

    [m,n] = P.shape

    M3=0
    M4=0
    for i in range(0,m):
        for j in range(0,n):
            Pr = P[i,j]
            Qr = Q[i,j]
            Pr = int (Pr)
            Pr = int (Qr)

            mag3 =abs ((Pr-Qr)**3)
            mag4 =abs ((Pr-Qr)**4)
            M3 = M3 + mag3
            M4 = M4 + mag4

    M3 = (M3/( (m)*(n) ))**(1/3)
    M4 = (M4/( (m)*(n) ))**(1/4)
    return (M3,M4)

####################################
image_file_name1 = sys.argv[1]
image_file_name2 = sys.argv[2]

image_name1 = io.imread(image_file_name1)
image_name2 = io.imread(image_file_name2)

print image_name1.shape
print image_name2.shape

[m,n] = image_name1.shape
[i,j] = image_name2.shape

print m,n,i,j


## estimate the image metrics

#estimate the peak signal to noise ratio (PSNR) between the image

peak_signal_to_noise_ratio = measure.compare_psnr (image_name1,image_name2)

print ("PSNR Peak signal to noise ratio is %s"%peak_signal_to_noise_ratio)

# estimate the mean square error between the images

mse = measure.compare_mse(image_name1,image_name2)

print  ("MSE Mean square error between the images is %s"%mse)

# estimate the normalised root mean square error between the images

rmse = measure.compare_nrmse(image_name1,image_name2)
print  ("RMSE Normalised root mean square error between the images is %s"%rmse)

ssim = measure.compare_ssim(image_name1,image_name2)
print ("SSIM Structural Similarity Index is %s"%ssim)

[M3,M4] = minkowski_distance(image_name1,image_name2)

print ("Minkowski distance is %s %s"%(M3,M4))

AD = average_difference(image_name1,image_name2)

print ("AD Average difference is %s"%AD)

SC = structural_content(image_name1,image_name2)

print ("SC Structural Content is %s"%SC)

NK = normalised_cross_correlation(image_name1,image_name2)

print ("NK normalised cross correlation is %s"%NK)

MD = maximum_difference(image_name1,image_name2)

print ("Maximum difference is %s"%MD)


