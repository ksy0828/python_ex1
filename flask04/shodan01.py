import shodan
import json

# Shodan API 키를 설정합니다.
SHODAN_API_KEY = 'B3D1KF0YfcNrkJRhdKxhh507EtZSA6fQ'
api = shodan.Shodan(SHODAN_API_KEY)

results = api.search('webcam')

print(f"검색 결과 : {results['total']}")

for match in results['matches'][:2]:
    print(f"IP       : {match['ip_str']}")
    print(f"PORT     : {match['port']}")
    print(f"ORG      : {match.get('org', 'n/a')}")
    print(f"LOCATION : {match['location']['country_name']}")
    print(f"HOSTNAME : {match['hostnames']}")

