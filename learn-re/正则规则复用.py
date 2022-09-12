import re

content1 = '2019-12-15 12:00'
content2 = '2219-12-15 12:00'
content3 = '2419-12-15 12:00'
# 把规则字符串编译一下，这样就可以复用了。如果在规则里加了re.S这样的修饰，findall search这些方法里就不用传了。
pattern = re.compile('\d{2}:\d{2}', re.S)
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)

print(result1, result2, result3)