
import sys
sys.path.append('./samplelib/')
import samplelib

import threading


class SomeThread(threading.Thread):

    def __init__(self, mode, *args):
        super(SomeThread, self).__init__()
        self.daemon = True

        self.mode = mode
        self.args = args
        self.result = None
        self.__instance = samplelib.SampleClass()

    def run(self):
        print('[Py] Thread started.')
        print('[Py] Before calling library function.')
        if self.mode == 0:
            self.result = self.__instance.run(*self.args)
        elif self.mode == 1:
            self.result = self.__instance.run_external(*self.args)
        else:
            self.result = self.__instance.run_thread_friendly_external(
                *self.args)
        print('[Py] After calling library function')


def run(thread):
    print('[Py] Before starting thread.')
    thread.start()
    print('[Py] After starting thread.')

    interval = 1
    while(1):
        thread.join(interval)
        print('[Py] Waiting!')
        if not thread.isAlive():
            print('[Py] Completed thread task.')
            print('[Py] Result: %d' % thread.result)
            break

    print('[Py] Completed.')


def main():
    print('=== Thread with Normal Function Call ===')
    foo = SomeThread(0, 5)
    run(foo)
    print('=== Thread With External Function Call ===')
    bar = SomeThread(1, 5)
    run(bar)
    print('=== Thread With External Function Call (Thread friendly) ===')
    baz = SomeThread(2, 5)
    run(baz)

if __name__ == '__main__':
    main()
