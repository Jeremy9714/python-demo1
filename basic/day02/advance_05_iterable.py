# 迭代器
# 可迭代对象需要实现__iter__方法，且该方法返回迭代器对象

from collections.abc import Iterable, Iterator

print(isinstance({1, 2, 3}, Iterable))

l1 = [1, 2, 3, 4, 5, 6, 7]
i1 = iter(l1)
print(i1)
print("----------------------------")

# 迭代器对象都是可迭代对象
# 可迭代对象拥有__iter__方法，迭代器对象拥有__iter__和__next__方法
print(isinstance(i1, Iterable))
print(isinstance(i1, Iterator))


class MyCounter:
    def __init__(self):
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.count >= 10:
            raise StopIteration('exceeds the limit')
        self.count += 1
        return self.count


c1 = MyCounter()
for i in c1:
    print(i)
