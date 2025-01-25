#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json
from datetime import datetime
from utils.env_path_util import client_id
from utils.env_path_util import client_secret
from utils.json_save_util import keyword_trend_result_save
url = "https://openapi.naver.com/v1/datalab/search"

all_data = []  # 모든 데이터를 저장할 리스트

try:
    competitor_keywords = {
        "원피스": [
            "롱원피스", "미니원피스", "플라워원피스", "오피스룩", "드레스", 
            "캐주얼원피스", "셔츠원피스", "여름원피스", "봄원피스", "가을원피스"
        ],
        "경량패딩": [
            "초경량패딩", "경량조끼", "경량점퍼", "겨울패딩", "바람막이",
            "다운패딩", "슬림패딩", "방풍자켓", "가을패딩", "경량아우터"
        ],
        "부츠": [
            "롱부츠", "앵클부츠", "첼시부츠", "가죽부츠", "스웨이드부츠",
            "미들부츠", "겨울부츠", "레이스업부츠", "타슬부츠", "숏부츠"
        ],
        "기모": [
            "기모맨투맨", "기모후드", "기모바지", "기모레깅스", "기모티셔츠",
            "기모코트", "기모스웨터", "기모원피스", "겨울기모", "보온기모"
        ]
    }
    keyword_groups = [
        {
            "groupName": competitor,
            "keywords": competitor_keywords[competitor]
        }
        for competitor in competitor_keywords
    ]

 
    body = {
        "startDate": "2024-08-01",
        "endDate": "2024-09-30",
        "timeUnit": "week",
        "keywordGroups": keyword_groups,
        "device": "pc", # 설정 안하면 pc,mo 전체 
        "gender": "m", # 설정 안하면 m,f 전체 
        "ages" : [f"{i}" for i in range(4,9)]
    }
    # print(body)

    body_json = json.dumps(body, ensure_ascii=False)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    response = urllib.request.urlopen(request, data=body_json.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()

        dataResult = json.loads(response_body.decode('utf-8'))
        data = dataResult['results']
        # print(data[0])
        keyword_trend_result_save(data[0])
        
    #     for item in data:
    #         item['data'] = [d for d in item['data'] if d['period'] == "2024-08-26"]

    #     # 데이터가 없으면 이전 날짜의 데이터를 가져오기
    #     if not item['data']:
    #         # 이전 날짜 데이터가 있는지 확인하고, 가장 최근 데이터를 선택
    #         previous_data = sorted(
    #             item['data'], 
    #             key=lambda x: datetime.strptime(x['period'], '%Y-%m-%d'), 
    #             reverse=True
    #         )
    #         if previous_data:
    #             item['data'] = previous_data[:1]  # 가장 최근 데이터만 남김
    #     all_data.extend(data)
    # # 비어 있지 않은 항목만 결과에 포함
    # result = [{'title': item['title'], 'ratio': item['data'][0]['ratio']} for item in data if item['data']]
    # max_ratio = max(item['ratio'] for item in result)
    # weighted_data = [{'title': item['title'], 'weight': round(item['ratio'] / max_ratio, 6)} for item in result]

    # ordered_data = sorted(weighted_data, key=lambda x: x['weight'], reverse=True)
    # titles = ', '.join([item['title'] for item in ordered_data])

except Exception as e:
    print(f"Error occurred for  {e}")
    
# print(all_data)
# # df.to_excel('ysj_20240923_4.xlsx', index=False)

