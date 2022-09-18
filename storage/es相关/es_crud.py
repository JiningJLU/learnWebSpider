from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='https://elastic:980909@localhost:9200', verify_certs=False)

data = {
    'title': 'Python',
    'content': 'Python is a programming language',
}
result = es.create(index='news', id=1, body=data)
# 也可以这么写, 自动指定Id
# result = es.index(index='news', document=data)
print(result)

data['title'] = 'Java'
result = es.index(index='news', id=1, document=data)
print(result)

result = es.delete(index='news', id=1)
print(result)