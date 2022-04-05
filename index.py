from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

print(es.info())

resp = es.search(index="customer", query={"match_all": {}}, sort=[
    {
        "name.keyword": {
            "order": "desc"
        }
    }
])

print(resp)
