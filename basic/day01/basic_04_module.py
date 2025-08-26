import string

from basic.day01.basic_03_exception import print_name

print_name()
print(__name__)  # 模块名称(主程序为__main__)


# 包(项目结构中的目录，含有__init__.py)

# 闭包
# 1) 内嵌函数
# 2) 内嵌函数引用了外部函数的局部变量
# 3) 外部函数返回值是内嵌函数
def counter(initial_val: int = 0) -> tuple:
    count = [initial_val]

    def increment():
        count[0] += 1
        return count[0]

    def decrement():
        count[0] -= 1
        return count[0]

    return increment, decrement


inc, dec = counter(10)
print(inc(), type(inc))
print(inc())
print(dec())


# 装饰器(将原有函数重新定义为以原有函数为入参的闭包)
def outer(fn):
    def inner():
        print("inner func invoked")
        fn()

    return inner


@outer  # @装饰器名称
def my_func():
    print("my_func invoked")


# inner = outer(my_func)
# inner()
my_func()

print("----------------------------")


def outer(fn):
    def inner(var: int = 10):
        print(f'var: {var}')
        print('inner func invoked')
        fn(var)

    return inner


@outer
def my_func(var: int):
    print(f"mu_func invoked, var is {var}")


# outer(my_func)(11)
my_func(123)

print("--------------------")


def test(a: int) -> string:
    return str(a)


print(test(12), type(test(12)))
print("----------------------")


def decor1(fn):
    def inner():
        return "decor1 invoked, " + fn() + " in decor1"

    return inner


def decor2(fn):
    def inner():
        return "decor2 invoked, " + fn() + " in decor2"

    return inner


@decor1
@decor2
def test() -> string:
    return 'test'


print(test())
