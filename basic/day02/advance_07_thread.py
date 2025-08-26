# 多线程
import time


def func1(name):
    print(f"func1 invoked by {name}")
    time.sleep(2)  # 挂起
    print("func1 terminated")


def func2(name):
    print(f"func2 invoked by {name}")
    time.sleep(2)
    print("func2 terminated")


# func1()
# func2()
print("-------------------------")

import threading  # 引入线程模块

# if __name__ == '__main__':
#     t1 = threading.Thread(target=func1, args=('Jeremy',))  # 创建子线程
#     t2 = threading.Thread(target=func2, args=('Sean',))
#
#     t1.setDaemon(True)  # 设置守护线程
#     t2.setDaemon(True)
#
#     t1.start()  # 开启子线程
#     t2.start()
#
#     # t1.join() # 挂起当前线程直到调用线程执行完毕
#     # t2.join()
#     print("main thread terminated")

# 互斥锁
from threading import Lock  # 引入锁

lock = Lock()  # 创建锁对象

num1 = 0
num2 = 1000000


def func3():
    global num1
    lock.acquire()  # 获取锁
    for i in range(num2):
        num1 += 1
    print(f"func3 invoked by thread {threading.current_thread().getName()}")
    print(num1)
    lock.release()  # 释放锁


def func4():
    global num1
    lock.acquire()
    for i in range(num2):
        num1 += 1
    print(f'func4 invoked by thread {threading.current_thread().getName()}')
    print(num1)
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=func3)
    t2 = threading.Thread(target=func4)

    t1.start()
    # t1.join()
    t2.start()
    # t2.join()
    print('main thread terminated')
