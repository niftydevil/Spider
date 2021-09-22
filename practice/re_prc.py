import re

ls = re.findall(r"\d+", "我的电话是：10086,另外一个电话是：10010")
print(ls)

ites = re.finditer(r"\d+", "我的电话是：10086,另外一个电话是：10010")
for ite in ites:
    print(ite)

s = re.search(r"\d+", "我的电话是：10086,另外一个电话是：10010")
print(s.group())

obj = re.compile(r"\d+")
result = obj.findall("我的电话是：10086,另外一个电话是：10010")
print(result)