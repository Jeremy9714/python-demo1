# 魔法方法

class Test:

    # 初始化新创建的实例对象
    def __init__(self, id):
        self.id = id
        print('__init__ method invoked')

    # 在内存中创建对象，并返回引用(在__init__方法前执行)
    def __new__(cls, *args, **kwargs):
        print('__new__ method invoked')
        return super().__new__(cls)


print(Test('123').id)
print('---------------------')


# 单例模式
class Singleton:
    obj = None

    def __new__(cls, *args, **kwargs):
        if Singleton.obj is not None:
            Singleton.obj = super().__new__(cls)
        return Singleton.obj
        # return super().__new__(cls)


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
print('-------------------------')


# 魔法方法
# 1) __doc__ 类或方法描述信息(多行注释)
class A:
    """
    doc for class A ...
    """

    sum = 0

    def method(self) -> None:
        """
        doc for method ...
        :return: None
        """
        pass

    def __str__(self):
        return 'class A'

    def __call__(self, *args, **kwargs):
        print('callable instance')
        self.sum += 1


print(A.__doc__)
print(A.method.__doc__)

# 2) __module__ 对象所属模块
print(A.__module__)

# 3) __class__ 对象所属类
print(A.__class__)

# 4) __str__ 对象描述信息
print(A())

# 5) __call__ 使实例对象成为可调用对象
print(callable(A()))  # callable判断对象是否可调用
a1 = A()
a1()
a1()
print(a1.sum)
print('-----------------')
