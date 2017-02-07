import callme
import subprocess 
import numpy as np
from PIL import Image
import code_exec
from code_exec import execute_user_script

def enveloppe_extract(func_str):
        import time
        import os
        print('toto')
        os.system('rm uploaded_custom.py | touch uploaded_custom.py')
        ret = open('uploaded_custom.py', 'wb')
        ret.write(func_str)
        ret.close()
        val_ret = {'score':10,'duration': 0}
        try:
            val_ret = execute_user_script()
            print(val_ret)            
        except:
            val_ret = {'score':0,'duration': 0}
        return val_ret


server = callme.Server(server_id='fooserver2',
                       amqp_host='localhost')

server.register_function(enveloppe_extract, 'enveloppe_extract')
server.start()
