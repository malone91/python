import threading


class MyThread(threading.Thread):
    def run(self):
        print(threading.current_thread().getName(), 'start')
        print('run')
        print(threading.current_thread().getName(), 'end')


t1 = MyThread()
t1.start()
t1.join()

print(threading.current_thread().getName(), 'main end')