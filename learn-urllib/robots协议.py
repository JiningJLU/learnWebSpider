from urllib.request import urlopen
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()

rp.set_url('https://www.baidu.com/robots.txt')
rp.read()

# 也可以这样写
# rp.parse(urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))
