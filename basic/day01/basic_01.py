a = 'Hello World'
print(a, type(a))
b = a.encode()
print(b, type(b))
c = b.decode()
print(c, type(c))

print(c * 5)
print('H' in c)
print(c[0:2])
print(c[:-1])
print(c[1:-2])
print(c[-1::-1])

l1 = ['A', '2', 'Three']
print(l1[-1::-1])
# for i in l1:
#     print(i)
l1.append("4")
l1.extend('ABC')
l1.insert(1, 'B')

# while len(l1) > 0:
#     print(l1.pop())

l1.remove("A")
l1.sort()
print(l1)

[print(i * 2) for i in l1]
l2 = []
[l2.append(i) for i in range(1, 10) if i % 2 != 0]
print(l2)

# 元组
t1 = (1,)
print(t1, type(t1))

name = "Jeremy"
age = 28
print("%s is about %d" % (name, age))
info = (name, age)
print(info, type(info))

# 字典
dict1 = {'k1': 'v1', 'k2': 'v2'}
print(dict1, type(dict1))
print(len(dict1))
keys = dict1.keys()
values = dict1.values()
print(keys, type(keys))
print(values, type(values))
for i in dict1.items():
    print(i, type(i))
print(dict1.popitem())

# 集合
s1 = {1, 2, 3, 2}
s2 = {'A', 'B', 'C'}
s1.add('C')
s1.update('DEF')
s2.discard('X')
print(s1, type(s1))
print(s2)

print(s1 & s2)
print(s1 | s2)

# eval执行字符串表达式 字符串和列表、元组、字典的转换
# age = input("type your age\n")
# print(age)
print(eval('10+20'))
print(eval("['A','B','C']"))
print(type(list('abcdef')))

# 深浅拷贝
l2 = ['A', 'B', 'C']
l3 = l2
l3.append('D')
l3.append([1,2,3])
print(id(l2))
print(id(l3))

import copy

l4 = copy.copy(l3)
l4.append('E')
l4[-2].append(4)
print(l3, id(l3))
print(l4, id(l4))

l5 = copy.deepcopy(l3)
l5.append('E')
l5[-2].append(5)
print(l3, id(l3))
print(l5, id(l5))
