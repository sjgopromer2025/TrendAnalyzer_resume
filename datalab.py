#-*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json
import pandas as pd
from datetime import datetime


client_id = "k7qMRMdftDjG9B6PKHPo"
client_secret = "hHbBDzvJb2"
url = "https://openapi.naver.com/v1/datalab/search";
# XLSX 파일 읽기
df = pd.read_excel('쓰레기.xlsx')
company_names = df['기업명'].tolist()
df['순위리스트'] = df['순위리스트'].astype(str)



for cp in company_names:
    try:
        competitor = df.loc[df['기업명'] == cp, '경쟁자'].values[0]
        if competitor in "정보없음":
            continue  
        competitor_list = [item.strip() for item in competitor.split(",")]
        competitor_list.append(cp)
        keyword_groups = [
            {
                "groupName": competitor,
                "keywords": [competitor]
            }
            for competitor in competitor_list
        ]

        body = {
            "startDate": "2024-08-01",
            "endDate": "2024-08-31",
            "timeUnit": "week",
            "keywordGroups": keyword_groups,
        }
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
            # print(data)
            for item in data:
                item['data'] = [d for d in item['data'] if d['period'] == "2024-08-26"]

            # 데이터가 없으면 이전 날짜의 데이터를 가져오기
            if not item['data']:
                # 이전 날짜 데이터가 있는지 확인하고, 가장 최근 데이터를 선택
                previous_data = sorted(
                    item['data'], 
                    key=lambda x: datetime.strptime(x['period'], '%Y-%m-%d'), 
                    reverse=True
                )
                if previous_data:
                    item['data'] = previous_data[:1]  # 가장 최근 데이터만 남김

            # 비어 있지 않은 항목만 결과에 포함
            result = [{'title': item['title'], 'ratio': item['data'][0]['ratio']} for item in data if item['data']]
            max_ratio = max(item['ratio'] for item in result)
            weighted_data = [{'title': item['title'], 'weight': round(item['ratio'] / max_ratio, 6)} for item in result]

            ordered_data = sorted(weighted_data, key=lambda x: x['weight'], reverse=True)
            titles = ', '.join([item['title'] for item in ordered_data])

            df.loc[df['기업명'] == cp, '순위리스트'] = titles

            if len(ordered_data) > 0:
                df.loc[df['기업명'] == cp, '1비중'] = ordered_data[0]['weight']
            if len(ordered_data) > 1:
                df.loc[df['기업명'] == cp, '2비중'] = ordered_data[1]['weight']
            if len(ordered_data) > 2:
                df.loc[df['기업명'] == cp, '3비중'] = ordered_data[2]['weight']
            if len(ordered_data) > 3:
                df.loc[df['기업명'] == cp, '4비중'] = ordered_data[3]['weight']
            if len(ordered_data) > 4:
                df.loc[df['기업명'] == cp, '5비중'] = ordered_data[4]['weight']
            if len(ordered_data) > 5:
                df.loc[df['기업명'] == cp, '6비중'] = ordered_data[5]['weight']
        else:
            print("Error Code:" + str(rescode))

    except Exception as e:
        print(f"Error occurred for {cp}: {e}")
        print("Competitor data:", competitor)
        
    
    
  
df.to_excel('ysj_20240923_4.xlsx', index=False)

