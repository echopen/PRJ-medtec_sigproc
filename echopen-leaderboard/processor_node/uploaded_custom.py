def install_packages():
    import pip
    pip.main(['install', 'numpy'])
    
def run(rawSignal,image_shape) :
    # Here is a copy of the baseline method. Replace that by another method.
    reconstructedImage = np.zeros(shape=(image_shape[0],image_shape[1]))
    decimationFactor = 1.0*rawSignal.shape[0]/image_shape[0]

    for i in range(rawSignal.shape[0]):
           for j in range(image_shape[1]):
                reconstructedImage[int(i/decimationFactor)][j] += np.abs(rawSignal[i][j])
    
    A = np.abs(reconstructedImage)
    A = A - A.min()
    A = 1.0*A/A.max()
    reconstructedImage = A    
    # The function should return the reconstructed image
    return reconstructedImage
