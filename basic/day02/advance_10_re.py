# 正则表达式
import re

# str1 = input('input your name\n')
# match() 从开始位置匹配，返回第一个匹配成功的结果
# res = re.match('\d+Jeremy', str1)
# print(res, res.group())  # 通过group()获取匹配结果

print(re.match('\w+', '中文').group())

print(re.match('[^Je]', 'remy'))  # []中的^表示取反

# \num 匹配分组num匹配到的字符串
print(re.match('<(div)>\d+</\\1>', '<div>123</div>'))

# (?P<name>)    分组起别名
# (?P=name)     引用指定别名分组匹配到的字符串
print(re.match('<(?P<s1>div)><(?P<s2>span)>\d+</(?P=s2)></(?P=s1)>', '<div><span>123</span></div>'))

print("-----------------------")

# 高级用法
# search() 扫描整个字符串并返回第一个匹配成功的对象，匹配失败则返回None
print(re.match('re', 'Jeremy'))
print(re.search('re', 'Jeremy'))

# findall() 以列表形式返回整个字符串中所有匹配到的结果
print(re.findall('e[r]?', 'Jeremy'))

# sub(pattern,repl,string,count) 将匹配到的数据进行替换
print(re.sub('\d+', '[num]', '12Sean714Jeremy', 2))

# split(pattern,string,maxsplit) 根据匹配结果分割字符串，并返回一个列表
print(re.split('\d+', 'Jeremy714Sean2', 1))

# 贪婪模式(默认使用)
# 在满足匹配时，匹配尽可能长的字符串
print(re.match('Je*', 'Jeeeeeeeeeeeeeeeeeeeeremy').group())

# 非贪婪模式
# 在满足匹配时，匹配尽可能短的字符串(使用?表示非贪婪匹配)
print(re.match('Je*?', 'Jeeeeeeeeeeeeeeeeeeeeremy').group())
print('-----------------------')

# 原生字符串
print(r'\n\t')
# 正则表达式中，使用\\\\用来匹配字符'\'
print(re.match('\\\\', r'\name').group())
print(re.match(r'\\', r'\name').group())
