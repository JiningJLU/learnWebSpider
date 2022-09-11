import requests, logging

# # 关闭库的异常
# from requests.packages import urllib3

# urllib3.disable_warnings()

# 也可以捕获异常到日志
# logging.captureWarnings(True)
response = requests.get('https://ssr2.scrape.center', verify=False)
print(response.status_code)