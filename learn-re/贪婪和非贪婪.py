import re

content = 'Hello 1234567 World_This is a Regex Demo'

result = re.match('^He.*(\d+).*Demo$', content)
# 只能输出7因为是贪婪的
print(result.group(1))
# 多了个? 非贪婪
result = re.match('^He.*?(\d+).*Demo$', content)

print(result.group(1))