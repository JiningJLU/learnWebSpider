from unittest import result
from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')

# 指定默认协议
# result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')

# 是否忽略fragment
# result = urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)

print(type(result))
print(result)