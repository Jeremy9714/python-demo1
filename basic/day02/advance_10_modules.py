# os模块
# 用于与操作系统交互
import os

# 使用的工作平台(操作系统类型)
print(os.name)  # windows返回nt, linux返回posix
# 读取环境变量
print(os.getenv('JAVA_HOME'))
# 分割目录名和文件名, 以元组形式接收
print(os.path.split(r'D:\Desktop\Games\ygocore\ocg-rule.pdf'))
# split元组第一个元素
print(os.path.dirname(r'D:\Desktop\Games\ygocore\ocg-rule.pdf'))
# split元组第二个元素
# 以\结尾报错；以/结尾返回空值
print(os.path.basename(r'D:\Desktop\Games\ygocore/'))
print(os.path.basename(r'D:\Desktop\Games\ygocore\ocg-rule.pdf'))
# 判断路径是否存在
print(os.path.exists(r'D:\Desktop\Games\ygocore/'))
# 判断路径是否存在文件
print(os.path.isfile(r'D:\Desktop\Games\ygocore/'))
# 判断路径是否存在目录
print(os.path.isdir(r'D:\Desktop\Games\ygocore/'))
# 获取绝对路径
print(os.path.abspath(r'advance_10_re.py'))
# 判断路径是否为绝对路径(不存在也不影响)
print(os.path.isabs(r'D:\Desktop\Games\ygocore2'))

print('------------------')

# sys模块
# 负责程序与解释器交互
import sys

# 获取系统默认字符集
print(sys.getdefaultencoding())
# 获取环境变量的路径(与解释器相关python.exe)
print(sys.path)  # 以列表形式返回，第一个元素为当前工作目录
# 获取操作系统平台名称
print(sys.platform)
# 获取解释器版本信息
print(sys.version)

print('-----------------')

# time模块
# 三种时间表示
# 1) 时间戳(timestamp)
# 2) 格式化时间字符串(format time)
# 3) 时间元组(struct_time)
import time

# 自1970/01/01 00:00:00至今的浮点型时间戳(s)
print(time.time())
# 获取系统当前时间，将时间戳转换为struct_time时间元组
print(time.localtime(), type(time.localtime()))
print(time.localtime(time.time()))
# 获取系统当前时间, 将struct_time时间元组转换为固定字符串表达式
print(time.asctime())
print(time.asctime(time.localtime()))
# 获取系统当前时间，将时间戳转换为固定字符串表达式
print(time.ctime())
print(time.ctime(time.time()))

# 将struct_time时间元组转换为时间字符串
print(time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime()))
# 将时间字符串转换为struct_time时间元组
print(time.strptime('2025-08-19 18:29:43', '%Y-%m-%d %H:%M:%S'))

print('--------------------')

# logging模块
# 日志信息(CRITICAL>ERROR>WARNING>INFO>DEBUG>NOTEST)
import logging

# 默认日志级别为Warning
# 日志配置
logging.basicConfig(filename='../logs/py.log',  # 指定日志存放文件
                    filemode='a',  # 写入模式
                    level=logging.DEBUG,  # 日志级别
                    format='%(asctime)s [%(thread)d] [%(levelname)s] %(name)s %(message)s')  # 日志格式

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

print('------------------')

# random模块
# 用于实现各种分布的伪随机数生成器
import random

# 生成[0,1)的小数
print(random.random())
# 生成指定范围内的小数([start, end))
print(random.uniform(0, 2))
# 生成指定范围内的整数([start, end])
print(random.randint(1, 2))
# 生成指定步长、范围内的整数([start, end [,step]))
print(random.randrange(0, 10, 2))
# 从非空序列中随机选一个元素
print(random.choice([1, 2, 3, 4]))
