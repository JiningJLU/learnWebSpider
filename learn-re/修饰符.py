import re

content = '''Hello 1234567 World_This
is a Regex Demo'''
# .*遇到换行符就结束了！
# 想要无视换行符，需要加re.S，代表匹配内容包含换行符
# re.S叫做修饰符，还有叫做re.I的修饰符，代表大小写不敏感
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))