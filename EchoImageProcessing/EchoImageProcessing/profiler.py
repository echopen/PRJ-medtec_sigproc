__author__ = 'mehdibenchoufi'

import time


class Profiler(object):

    def __init__(self):
        print 'prepare to profile...'

    def __enter__(self):
        self.echo_start = time.time()
        return self

    def __exit__(self, *args):
        self.echo_end = time.time()
        self.ms = (self.echo_end - self.echo_start) * 1000
