import threading
import time


def myhread(arg1, arg2):
    print(threading.current_thread().getName(), 'start')
    print(arg1, arg2)


for i in range(1, 6, 1):
    myhread(i, i + 2)

for i in range(1, 6, 1):
    t1 = threading.Thread(target=myhread, args=(i, i+1))
    time.sleep(0.3)
    t1.start()


print(threading.current_thread().getName(), 'main end')
