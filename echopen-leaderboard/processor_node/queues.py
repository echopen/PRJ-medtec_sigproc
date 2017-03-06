from kombu import Exchange, Queue

task_exchange = Exchange('tasks', type='direct')
task_queues = [Queue('echopen', task_exchange, routing_key='denoise')]
