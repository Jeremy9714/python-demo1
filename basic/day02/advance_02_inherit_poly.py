# 多继承(子类可以拥有多个父类)
import string


class Shape:
    # pass  # 占位符
    def info(self):
        print('this is a shape')


class Triangle(Shape):
    def info(self):
        # super().info()
        super(Triangle, self).info()  # 父类方法
        print('this is a triangle')


t1 = Triangle()
t1.info()
print('-----------------')


class A:
    token = 'A'

    def test(self):
        print('A')


class B:
    token = 'B'

    def test(self):
        print('B')


# 多个父类存在同名属性或方法，前面的优先级高
class C(A, B):
    pass


c1 = C()
c1.test()
print(c1.token)
print(C.__mro__)  # 查看方法搜索顺序
print('---------------------')


# 静态方法
class Test:
    token = 'Test'

    @staticmethod
    def printMsg(msg: string):
        # print(Test.token)
        print(msg)


Test().printMsg('msg')
Test.printMsg('msg')
print('-------------------')


# 类方法(第一个参数为类对象cls)
class Test2:
    token = 'Test2'

    @classmethod
    def printMsg(cls):
        print(cls)
        print(cls.token)


Test2.printMsg()
