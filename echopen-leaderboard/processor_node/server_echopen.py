import callme
import subprocess 

def denoise(func_str):
        import time
        import os
        os.system('rm uploaded_custom.py | touch uploaded_custom.py')
        ret = open('uploaded_custom.py', 'wb')
        ret.write(func_str)
        ret.close()
        try:
	    from metrics import run_metrics
            val_ret = {'score':0,'duration': 0}
            ret = subprocess.check_output('python uploaded_custom.py', shell=True)
            import code_exec
            from code_exec import execute_user_script
            import glob
            denoise_list = glob.glob('./kaggle/*_*.jpg')
            total_list = glob.glob('./kaggle/*.jpg')
            raw_list= list(set(total_list) - set(denoise_list))
            print raw_list
            run_duration = execute_user_script(raw_list)
            for i in raw_list:
                        print i
                        tmp  = run_metrics(i, os.path.split(i)[0]+'/denoise_'+os.path.split(i)[1])
                        val_ret['score'] += tmp['score']
            val_ret['duration'] = run_duration
            return val_ret            
        except Exception as  e:
           print e
        return val_ret

server = callme.Server(server_id='fooserver2',
                       amqp_host='amqp://echopen1:echopen1@37.187.117.106/echopen1')

server.register_function(denoise, 'denoise')
server.start()
