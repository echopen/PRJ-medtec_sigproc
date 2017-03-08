def install_packages():
    import pip
    pip.main(['install', 'aesop'])

def run():
    print('toto')
    import io
    import os
    import sys
    import argparse
    from skimage import io
    from skimage import filter
    from skimage import restoration
    from skimage import measure

    kidney_image = io.imread('manu.jpg')
    # estimate the noise in the image
    # do a test denosing using a total variation filter
    kidney_image_denoised_tv = restoration.denoise_tv_chambolle( kidney_image, weight=0.1)
    io.imsave('denoise_image.jpg', kidney_image_denoised_tv)




