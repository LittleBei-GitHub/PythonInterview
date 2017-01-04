# coding=utf-8
import threading
import time

## 在函数中使用多线程
def run(num):
    print('thread: %d' %num)

def main_1():
    threads=[]
    for i in range(5):
        t=threading.Thread(target=run, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


## 在类中使用多线程
lock=threading.Lock()
class Thread_1(threading.Thread):
    def __init__(self, num):
        self.num=num
        super(Thread_1, self).__init__()

    def run(self):
        #lock.acquire()
        print('thread %d' %self.num)
        #time.sleep(1)
        #lock.release()

def main_2():
    threads=[]
    for i in range(5):
        t=Thread_1(i)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


## 线程同步与互斥锁
var=0
class Thread_2(threading.Thread):
    def run(self):
        lock.acquire()
        global var

        print('before var is %d' %var)
        var+=1
        print('after var is %d ' %var)
        lock.release()

def main_3():
    threads=[]
    for i in range(10):
        t=Thread_2()
        threads.append(t)
        t.start()
    for t in threads:
        t.join()



if __name__ == '__main__':
    # print('start...')
    # main_1()
    # print('end...')

    # print('start...')
    # main_2()
    # print('end...')

    print('start...')
    main_3()
    print('end...')