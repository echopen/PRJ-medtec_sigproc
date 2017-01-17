from kombu.mixins import ConsumerMixin
from kombu.log import get_logger
#from kombu.utils import kwdict, reprcall
import subprocess
from queues import task_queues

logger = get_logger(__name__)


class Worker(ConsumerMixin):

    def __init__(self, connection):
        self.connection = connection

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=task_queues,
                         callbacks=[self.process_task])]

    def process_task(self, body, message):
        import time
        import os
        print body, message
        os.system('rm uploaded_custom.py | touch uploaded_custom.py')
        ret = open('uploaded_custom.py', 'wb')
        ret.write(body)
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
            run_duration = execute_user_script(raw_list)
            for i in xrange(1,40):
                tmp  = run_metrics('./kaggle/'+str(i)+'.jpg', './kaggle/denoise_'+str(i)+'.jpg')
                print i, tmp['score']
                val_ret['score'] += tmp['score']
            val_ret['duration'] = run_duration
            return 

        except Exception as exc:
            logger.error('task raised exception: %r', exc)
        message.ack()


if __name__ == '__main__':
    from kombu import Connection
    from kombu.utils.debug import setup_logging
    # setup root logger
    setup_logging(loglevel='INFO', loggers=[''])

    with Connection('amqp://echopen1:echopen1@37.187.117.106/echopen1') as conn:
        try:
            worker = Worker(conn)
            worker.run()
        except KeyboardInterrupt:
            print('bye bye')
