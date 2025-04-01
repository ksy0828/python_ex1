import shodan
from pymongo import MongoClient

# Shodan API 키를 설정합니다.
SHODAN_API_KEY = 'B3D1KF0YfcNrkJRhdKxhh507EtZSA6fQ'
api = shodan.Shodan(SHODAN_API_KEY)


#DB 연결
client = MongoClient('mongodb://localhost:27017') 
db = client['shodan_db']
collection = db['webcam_results']

#쇼단에 웹캠 검색
results = api.search('webcam')
print(f"검색 결과 : {results['total']}")

for match in results['matches'][:3]:
    data = {
        "IP": match['ip_str'],
        "PORT": match['port'],
        "ORG": match.get('org', 'n/a'),
        "LOCATION": match['location']['country_name'],
        "HOSTNAME": match['hostnames']
    }
    collection.insert_one(data)
    print(f"저장된 IP : {match['ip_str']}")