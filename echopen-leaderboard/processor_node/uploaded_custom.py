def install_packages():

    import pip

    pip.main(['install', 'scipy'])

    

def run(rawSignal,image_shape) :

    import numpy as np

    reconstructedImage = np.zeros(shape=(image_shape[0],image_shape[1]))

    #print (image_shape)

    decimationFactor = 1.0*rawSignal.shape[0]/image_shape[0]

    #print(decimationFactor)

    for j in range(image_shape[1]): 

        for i in range(image_shape[0]):

            m = 0

            Dec = (int)(decimationFactor)

            for k in range(Dec):

                if np.abs(rawSignal[int(decimationFactor*i)+k][j]) > m:

                    m = np.abs(rawSignal[int(decimationFactor*i)+k][j])

                    

            reconstructedImage[i][j] = m

                

    reconstructedImage = normImag(np.abs(reconstructedImage))
    return reconstructedImage
