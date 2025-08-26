# 生成器
# 生成器是一种特殊的迭代器，它使用yield关键字来产生值。
# 生成器函数在调用时不会立即执行，而是返回一个生成器对象

l1 = [i for i in range(1, 10)]
print(l1)

g1 = (i for i in range(1, 10))  # 生成器
print(g1)
print(next(g1))
print("---------------------")

l1 = []


def gen(num):
    i = 0
    while i < num:
        l1.append(i)
        yield i  # 返回一个生成器，延迟计算结果
        i += 1


g1 = gen(10)
print(g1)
for i in g1:
    print(l1)
