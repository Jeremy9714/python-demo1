# 协程(coroutine)
# 协程是一种可以暂停和恢复的函数. 它可以被理解为子程序的一种泛化

# greenlet
# 第三方协程模块, 通过switch()实现函数之间的切换; IO时程序挂起, 无法通过switch()切换
from greenlet import greenlet

#
# def func1():
#     print('func1 been invoked')
#     g2.switch()
#     print('func1 terminated')
#
#
# def func2():
#     print("func2 been invoked")
#     print('func2 terminated')
#     g1.switch()
#
#
# if __name__ == '__main__':
#     g1 = greenlet(func1)  # 创建协程对象
#     g2 = greenlet(func2)
#     # g1.switch()  # 切换到指定方法运行
#     g2.switch()

# gevent
# 第三方协程模块, 遇到IO操作时, 自动进行切换
import gevent
import time


def func3():
    print('func3 been invoked')
    # time.sleep(2)
    gevent.sleep(2)  # 模拟IO, 会自动切换协程
    print('func3 terminated')


def func4():
    print('func4 been invoked')
    # time.sleep(3)
    gevent.sleep(3)
    print('func4 terminated')


def func5(name):
    for i in range(1, 4):
        gevent.sleep(1)
        print(f'{i} times func5 been invoked by {name}')


from gevent import monkey  # 拥有在模块运行时替换的功能

# monkey模块自动将time.sleep替换为gevent耗时操作(gevent.sleep)
monkey.patch_all()  # 必须放在被打补丁的对象前面


def func6(name):
    for i in range(3):
        time.sleep(1)
        print(f'{i + 1} times func6 been invoked by {name}')


if __name__ == '__main__':
    # g3 = gevent.spawn(func3)  # 创建协程对象
    # g4 = gevent.spawn(func4)
    # g3.join()  # 阻塞直至协程对象执行完毕
    # g4.join()

    # gevent.joinall([  # 等待所有协程对象执行完毕再退出
    #     gevent.spawn(func5, 'Jeremy'),
    #     gevent.spawn(func5, 'Sean')
    # ])

    gevent.joinall([
        gevent.spawn(func6, 'Jeremy'),
        gevent.spawn(func6, 'Sean')
    ])

    print('---------------------------')

"""
1) 进程: 切换所需的资源最大，效率最低；多进程适合CPU密集型操作(科学计算、视频解码)
2) 线程: 切换所需的资源一般，效率一般；多线程适合IO密集型操作(文件操作、爬虫)
3) 协程: 切换所需的资源最小，效率最高
"""
