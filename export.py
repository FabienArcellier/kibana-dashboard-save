import sys, urllib, json

if len(sys.argv) < 2 :
    print("usage :  python %s http://localhost:9200 > file.json" % (sys.argv[0]))
    exit()

elasticsearch_url = sys.argv[1]
query_url = elasticsearch_url + "/.kibana/_search?q=*&size=10000"
response = urllib.urlopen(query_url)
data = json.loads(response.read())
dashboards = data['hits']['hits']

print(json.dumps(dashboards, sort_keys=True, indent=4))
