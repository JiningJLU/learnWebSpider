import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra     Strings'
# search可以从任何位置开始。所以注意不要加^和$
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result.group())

# 匹配所有可以用findall