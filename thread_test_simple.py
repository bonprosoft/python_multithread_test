
import sys
sys.path.append('./samplelib/')
import samplelib
import threading


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
            break

    print('[Py] Completed.')


def main():
    instance = samplelib.SampleClass()
    print('=== Thread with Normal Function Call ===')
    foo = threading.Thread(target=instance.run, args=(5,))
    run(foo)
    print('=== Thread With External Function Call ===')
    bar = threading.Thread(target=instance.run_external, args=(5,))
    run(bar)
    print('=== Thread With External Function Call (Thread friendly) ===')
    baz = threading.Thread(
        target=instance.run_thread_friendly_external, args=(5,))
    run(baz)

if __name__ == '__main__':
    main()
