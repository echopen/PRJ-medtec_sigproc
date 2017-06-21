import ast
import pip, time
import numpy as np
from PIL import Image
import traceback


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


def reconstructBaseline(rawSignal,image_shape) :
    reconstructedImage = np.zeros(shape=(image_shape[0],image_shape[1]))
    decimationFactor = 1.0*rawSignal.shape[0]/image_shape[0]

    for i in range(rawSignal.shape[0]):
           for j in range(image_shape[1]): 
                reconstructedImage[int(i/decimationFactor)][j] += np.abs(rawSignal[i][j])
                
    reconstructedImage = normImag(np.abs(reconstructedImage))
    return reconstructedImage

def execute_enveloppe():
    im = Image.open("fantom.bmp").convert('L') # convert 'L' is to get a flat image, not RGB
    groundTruth = normImag(np.array(im))
    rawSignal = np.loadtxt("SinUs.csv.gz", delimiter=';')
    recon = submit_function.reconstructImage(rawSignal,groundTruth.shape)
    [score,maxErr] = estimateScore(groundTruth, recon)
    print('Score for Baseline method : ', score)
    print('max Err between pixels for Baseline method : ', maxErr)

def execute_user_script():
    import sys 
    val_ret = {'duration':'0','score':'10000'}
    f = open("uploaded_custom.py", "r")
    data = f.read()

    try:
        tree = ast.parse(data)
    except Exception as e:      
        val_ret['error_msg'] = e.strerror
        return val_ret
    # tree.body[0] contains FunctionDef for fun1, tree.body[1] for fun2

    str_func = ""
    run_func = ""

    for function in tree.body:
        if isinstance(function,ast.FunctionDef):
            # Just in case if there are loops in the definition
            lastBody = function.body[-1]
            while isinstance (lastBody,(ast.For,ast.While,ast.If)):
                lastBody = lastBody.Body[-1]
            lastLine = lastBody.lineno
            if function.name == 'install_packages' :
                st = data.split("\n")
                for i , line in enumerate(st,1):
                    if i in range(function.lineno,lastLine+1):
                        str_func = str_func +'\n'+ line


            elif function.name == 'run':
                st = data.split("\n")
                for i , line in enumerate(st,1):
                    if i in range(function.lineno,lastLine+1):
                        run_func = run_func +'\n'+ line



    exec str_func
    exec run_func

    val_ret = {'duration':'0','score':'10000', 'error_msg':'None'}
    im = Image.open("fantom.bmp").convert('L') # convert 'L' is to get a flat image, not RGB
    groundTruth = normImag(np.array(im))
    rawSignal = np.loadtxt("SinUs.csv.gz", delimiter=';')
    print 'install packages'

    try:
        install_packages()

    except Exception as e:
        val_ret['error_msg'] = 'ERROR in PACKAGES INSTALLATION :' + str(e)
        print('ERROR in PACKAGES INSTALLATION' + str(e))
        return val_ret

    print 'install done'
    start = time.clock()
    print 'execute user script'

    try:
        recon = run(rawSignal, groundTruth.shape)
    except Exception as e:
        print('ERROR in CODE EXECUTION :' + str(e))
        val_ret['error_msg'] = 'ERROR in CODE EXECUTION :' + str(e)
        return val_ret

    end = time.clock()
    [score,maxErr] = estimateScore(groundTruth, recon)
    val_ret["duration"] = (end - start)
    val_ret["score"] = score
    print val_ret
    return val_ret

