from __future__ import print_function
import numpy as np
from PIL import Image # for bmp import
from glob import glob
from scipy.misc import imresize
import matplotlib.pyplot as plt
import math
import time



def showImage(imageToPlot):
    plt.figure(figsize=(2, 4))
    plt.gray()
    plt.imshow(imageToPlot.reshape(imageToPlot.shape), aspect='auto')
    plt.show()

def normImag(A):
# Let's normalize the image
    A = A - A.min()
    A = 1.0*A/A.max()
    return(A)


def ssd(A,B):
    A = A - 0.95*A.min()
    A = 1.0*A/A.max()
    B = B - 0.95*B.min()
    B = 1.0*B/B.max()
    squares = (A[:,:] - B[:,:]) ** 2
    return np.sum(squares)

def estimateScore(groundTruth, reconstructedImage) :
    errorMap = (groundTruth - reconstructedImage)
    print('Error map between ground truth and reconstructed image : ')
    showImage(errorMap)
    score = ssd(reconstructedImage,groundTruth)
    maxErr = errorMap.max()
    return [score,maxErr]

def compareImages(im1,im2) :
    plt.figure()
    ax = plt.subplot(1, 2, 1)
    plt.imshow(im1)
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax = plt.subplot(1, 2, 2)
    plt.imshow(im2)
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()


if __name__ == '__main__' :
	im = Image.open("fantom.bmp").convert('L') # convert 'L' is to get a flat image, not RGB
    groundTruth = normImag(np.array(im)) # we use the full [0;1] range
    showImage(groundTruth)
