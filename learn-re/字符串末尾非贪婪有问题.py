import re

content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)
print(result1.group(1))
print(result2.group(1))

# result1:
# result2: kEraCN
# result1的那个?导致后面的字符直接不匹配了。