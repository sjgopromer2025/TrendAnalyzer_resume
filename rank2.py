# 주어진 데이터
data = [
  {
    "title": "버거킹",
    "keywords": ["버거킹"],
    "data": [{ "period": "2024-08-26", "ratio": 78.55394 }]
  },
  {
    "title": "맘스터치",
    "keywords": ["맘스터치"],
    "data": [{ "period": "2024-08-26", "ratio": 78.92173 }]
  },
  {
    "title": "노브랜드버거",
    "keywords": ["노브랜드버거"],
    "data": [{ "period": "2024-08-26", "ratio": 23.32495 }]
  },
  {
    "title": "롯데리아",
    "keywords": ["롯데리아"],
    "data": [{ "period": "2024-08-26", "ratio": 86.83413 }]
  },
  {
    "title": "KFC",
    "keywords": ["KFC"],
    "data": [{ "period": "2024-08-26", "ratio": 36.53397 }]
  },
  {
    "title": "서브웨이",
    "keywords": ["서브웨이"],
    "data": [{ "period": "2024-08-26", "ratio": 82.50937 }]
  },
  {
    "title": "퀴즈노스",
    "keywords": ["퀴즈노스"],
    "data": [{ "period": "2024-08-26", "ratio": 6.93671 }]
  },
  {
    "title": "죠샌드위치앤커피",
    "keywords": ["죠샌드위치앤커피"],
    "data": [{ "period": "2024-08-26", "ratio": 0.00000002 }]
  },
  {
    "title": "뉴욕버거",
    "keywords": ["뉴욕버거"],
    "data": [{ "period": "2024-08-26", "ratio": 10.75204 }]
  },
  {
    "title": "비스트로피자",
    "keywords": ["비스트로피자"],
    "data": [{ "period": "2024-08-26", "ratio": 1.14086 }]
  },
  {
    "title": "에그샐런트",
    "keywords": ["에그샐런트"],
    "data": [{ "period": "2024-08-26", "ratio": 0.64532 }]
  },
  {
    "title": "쉐이크쉑",
    "keywords": ["쉐이크쉑"],
    "data": [{ "period": "2024-08-26", "ratio": 100 }]
  }
]


# 제목과 ratio를 포함하는 새로운 리스트 생성
result = [
    {'title': item['title'], 'ratio': item['data'][0]['ratio']}
    for item in data
]

# 1등의 ratio를 1로 설정하고 나머지 항목들의 ratio 기반으로 가중치 계산
max_ratio = max(item['ratio'] for item in result)
weighted_data = [{'title': item['title'], 'weight': round(item['ratio'] / max_ratio, 6)} for item in result]

# 가중치를 포함하여 결과 리스트 생성
for i in range(len(result)):
    result[i]['weight'] = weighted_data[i]['weight']

# ratio 기준으로 정렬
result.sort(key=lambda x: x['ratio'], reverse=True)

# 순위 매기기
for rank, item in enumerate(result, start=1):
    item['rank'] = rank

# 결과 출력
print(result)
for i in result:
    print(i["title"], ",", i["rank"], ",", i["weight"])