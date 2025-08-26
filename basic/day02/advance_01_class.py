# 类
class Student:
    id = '123'
    name = 'Jeremy'

    def __init__(self, gender):  # 构造函数
        self.gender = gender
        print('init method invoked')

    def info(self):
        print(Student.id, Student.name, self.gender)

    def __del__(self):  # 析构函数
        print('del method invoked')


s1 = Student('male')
s1.info()
print(s1, type(s1))
del s1

print('-----------------')


# 隐藏属性/方法(__xx)
# 私有属性/方法(_xx)
class Employee:
    __name = 'Sean'  # 隐藏属性, 子类不继承
    age = 28
    _gender = 'male'  # 私有属性, 子类继承

    def info(self):
        print(Employee.__name, Employee.age, Employee._gender)  # 内部访问私有属性
        self.__secret()

    def __secret(self):
        print('__xx invoked')


e1 = Employee()
print(e1._Employee__name)  # 外部访问隐藏属性(不正规) _class__attribute
# e1._Employee__secret()
print(e1._gender)
e1.info()
