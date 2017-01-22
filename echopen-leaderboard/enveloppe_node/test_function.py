import numpy as np
from PIL import Image

import submit_function

def normImag(A):
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
    score = ssd(reconstructedImage,groundTruth)
    maxErr = errorMap.max()
    return [score,maxErr]

im = Image.open("fantom.bmp").convert('L') # convert 'L' is to get a flat image, not RGB
groundTruth = normImag(np.array(im))
rawSignal = np.loadtxt("SinUs.csv.gz", delimiter=';')

recon = submit_function.reconstructImage(rawSignal,groundTruth.shape)
[score,maxErr] = estimateScore(groundTruth, recon)

print('Score for Baseline method : ', score)
print('max Err between pixels for Baseline method : ', maxErr)
