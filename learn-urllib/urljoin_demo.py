from urllib.parse import urljoin

# base_url(前面那个)提供了scheme netloc path，如果后面的url没有这些项，就从前面的里面进行对应的补充。
print(urljoin('https://www.baidu.com', 'FAQ.html'))
print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('https://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('https://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))