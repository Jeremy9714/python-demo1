# 进程
from multiprocessing import Process  # 引入进程
import os


def func1():
    print("func1 invoked")
    print('ppid', os.getppid())  # 获取父进程id


def func2():
    print("func2 invoked")


# if __name__ == '__main__':
#     p1 = Process(target=func1, name='p1')
#     p2 = Process(target=func2, name='p2')
#     p1.start()
#     p2.start()
#     print(p1.name, p1.pid)
#     print(p2.name, p2.pid)
#
#     print('main', os.getpid())  # 获取主进程id
#     print("------------------------")


# 进程之间不共享全局变量
from multiprocessing import Queue

# q1 = Queue(3)  # 队列大小
# q1.put('A')
# q1.put('B')
# q1.put('C')
# print('size: ', q1.qsize())
# print('isFull: ', q1.full())  # 是否满队列
# print(q1.get())
# print('isFull: ', q1.full())
# q1.get()
# q1.get()
# print('isEmpty: ', q1.empty())  # 是否空队列

print('-----------------------')

import time


def writer(q: Queue):
    for i in range(10):
        q.put(i)
        print(f'put {i} into queue')
        time.sleep(0.1)


def reader(q: Queue):
    while not q.empty():
        print(f'retrieve {q.get()} from queue')


if __name__ == '__main__':
    q2 = Queue()  # 进程间通信Queue
    p1 = Process(target=writer, args=(q2,))
    p2 = Process(target=reader, args=(q2,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
