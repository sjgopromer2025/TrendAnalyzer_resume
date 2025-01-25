import urllib.request
import json

# 네이버 애플리케이션에서 발급받은 클라이언트 ID와 Secret
client_id = "YOUR_CLIENT_ID"  # 네이버 개발자 센터에서 발급받은 ID로 변경
client_secret = "YOUR_CLIENT_SECRET"  # 네이버 개발자 센터에서 발급받은 Secret으로 변경

# API URL
url = "https://openapi.naver.com/v1/datalab/shopping/categories"

# 요청 본문 데이터
body = {
    "startDate": "2017-08-01",  # 시작 날짜
    "endDate": "2017-09-30",    # 종료 날짜
    "timeUnit": "month",        # 구간 단위 (date, week, month 중 하나)
    "category": [
        {"name": "패션의류", "param": ["50000000"]},
        {"name": "화장품/미용", "param": ["50000002"]}
    ],
    "device": "pc",             # 검색 기기 (pc, mo, 미설정시 모든 기기)
    "ages": ["20", "30"],       # 연령대
    "gender": "f"               # 성별 (f: 여성, m: 남성, 미설정시 모든 성별)
}

# 요청 객체 생성
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
request.add_header("Content-Type", "application/json")

try:
    # API 호출
    response = urllib.request.urlopen(request, data=json.dumps(body).encode("utf-8"))
    rescode = response.getcode()
    
    if rescode == 200:  # HTTP 상태 코드 200: 성공
        response_body = response.read()
        result = json.loads(response_body)  # JSON 형식으로 변환
        print(json.dumps(result, indent=4, ensure_ascii=False))  # 결과를 보기 좋게 출력
    else:
        print("Error Code:", rescode)

except Exception as e:
    print("Exception occurred:", e)





tt= "u넥패딩조끼 남성후드패딩조끼 내셔널패딩조끼 다운패딩조끼 브랜드패딩조끼 등산패딩조끼 아방패딩조끼 융털패딩조끼 여성패딩조끼"

print(tt.replace(" ","\n"))