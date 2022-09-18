from elasticsearch import Elasticsearch
# es = ElasticSearch(['https://[username:password@]hostname:port'], verify_certs=True)
es = Elasticsearch(hosts='https://elastic:980909@localhost:9200', verify_certs=False)

# 忽略400错误
result = es.indices.create(index='news', ignore=400)
print(result)

result = es.indices.delete(index='news', ignore=[400, 404])
print(result)
