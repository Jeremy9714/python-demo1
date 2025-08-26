# 返回元组
def func1():
    return 'A', 10


result = func1()
print(result, type(result))


def func2(x, y):
    return x, y


print(func2(1, 2))


# 参数默认值(默认参数放后面)
def func3(a, b=2, c=3):
    return a + b + c


print(func3(10, 11))


# 可变参数(以元组形式接受)
def func4(*args):
    print(type(args))
    total = 0
    for i in args:
        total += i
    return total


print(func4(1, 2, 3, 4, 5))


# 关键字参数(以字典形式接收)
def func5(**kwargs):
    print(kwargs, type(kwargs))


func5(name='Jeremy', age=28, gender='male')


# 嵌套函数
def func6():
    print(6)


def func7():
    func6()
    print(7)


func7()

var1 = 10
print('var1: %s' % var1)


def func8():
    global var1, var2  # 声明全局变量
    var1 = 12
    var2 = 13
    print('var1: %s' % var1)


func8()
print('var1: %s\tvar2: %s' % (var1, var2))


def outer():
    var1 = 10

    def inner():
        nonlocal var1  # 声明上一层局部变量
        var1 = 20
        print(f'inner: {var1}')

    inner()
    print(f'outer: {var1}')


outer()

# 匿名函数(lambda)
func = lambda a, b: a + b
print(func(1, 2))
func = lambda: 'no args function'  # 无参
print(func())
func = lambda a, b=1: a + b  # 默认参数
print(func(1))
func = lambda **kwargs: kwargs
print(func(name='Jeremy', age=28))
func = lambda a, b: 'a<b' if a < b else 'a>=b'
print(func(1, 2))

# 内置函数
import builtins

print(dir(builtins))

from functools import reduce

addFunc = lambda a, b: a + b
print(reduce(addFunc, [1, 2, 3, 4, 5, 6, 7]))

tuple1 = (1, 2, 3, 4)
a, b, c, d = tuple1
print(f'a:{a}\tb:{b}\tc:{c}\td:{d}')
a, *tuple2 = tuple1
print('a:', a, '\ttuple2:', tuple2, type(tuple2))
