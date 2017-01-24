import callme
import subprocess

def enveloppe_extract(func_str):
        import time
        import os
        os.system('rm uploaded_custom.py | touch uploaded_custom.py')
        ret = open('uploaded_custom.py', 'wb')
        ret.write(func_str)
        ret.close()
        try:
            val_ret = {'score':0,'duration':10}
        except:
            pass
        return val_ret

server = callme.Server(server_id='fooserver2',
                       amqp_host='amqp://echopen1:echopen1@37.187.117.106/echopen1')

server.register_function(enveloppe_extract, 'enveloppe')
server.start()
