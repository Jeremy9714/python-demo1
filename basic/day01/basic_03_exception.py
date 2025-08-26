# 异常处理
# raise Exception('illegal input')  # 抛出异常

try:
    result = 10 / 0
except Exception as e:
    print(e)


def print_name():
    print(__name__)
