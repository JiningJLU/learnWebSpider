import re

content = '54aK54yr5oiR54ixL2g'
content = re.sub('\d+', '', content)
print(content)
