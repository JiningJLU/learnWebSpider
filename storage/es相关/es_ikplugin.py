from elasticsearch import Elasticsearch

es = Elasticsearch(hosts='https://elastic:980909@localhost:9200', verify_certs=False)

mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'ik_max_word',
            'search_analyzer': 'ik_max_word',
        }
    }
}

es.indices.delete(index='news', ignore=[400, 404])
es.indices.create(index='news', ignore=400)
result = es.indices.put_mapping(index='news', body=mapping)
print(result)