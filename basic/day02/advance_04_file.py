# 文件读写
# file = open('../files/1.txt', 'r+t', encoding='UTF-8')  # 先写再读取 覆盖原文件内容
# file = open('../files/1.txt', 'w+t', encoding='UTF-8')  # 先写再读取 删除原文件内容
file = open('../files/1.txt', 'a+t', encoding='UTF-8')  # 先追加再读取 不删除原文件内容
# file = open(r'D:\workplace\2021-2024\workplace\python\demo2\basic\files\1.txt', 'rt')
print(f'{file.name} in mode {file.mode}')

# print(file.read(10))
# print(file.readline(-1))
# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line)

file.write('\ngo')
print(file.tell())  # 文件指针位置

# seek(offset, whence)
# offset: 偏移量 要移动的字节数
# whence: 移动字节参考位置 0代表文件开头位置 1代表当前位置 2代表文件末尾位置
file.seek(0, 0)

# 遍历文件内容
for line in file.readlines():
    print(line.strip('\n'))

print()
# print(file.readlines())

if not file.closed:
    file.close()
print(file.closed)

print('-------------------------')

# with open 自动调用close
with open('../files/1.txt', 'a+t', encoding='UTF-8') as file:  # encoding指定字符集
    file.write('\n末尾')
    file.seek(0, 0)
    for line in file.readlines():
        print(line.strip('\n'))
print(file.closed)

# 复制图片
with open('../files/6.png', 'rb') as source:
    # print(source.read())
    with open('../files/7.png', 'wb') as target:
        for line in source.readlines():
            target.write(line)

print('---------------------')

# os模块
import os

print(os.path.exists('../files'))  # 判断路径是否存在
print(os.getcwd())  # 获取当前路径
print(os.listdir('.'))  # 获取目录列表
# os.rename('','')  # 文件重命名
# os.remove('')  # 删除文件
# os.mkdir('') # 创建目录
# os.rmdir('') #  删除目录
