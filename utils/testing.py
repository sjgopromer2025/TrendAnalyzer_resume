import json
import os

class CategoriesData:
    def __init__(self, json_data):
        """
        JSONTreeVisualizer 초기화 메서드
        :param json_data: 트리 구조로 변환할 JSON 데이터 (딕셔너리 형태)
        """
        self.json_data = json_data
     

    def test(self):
        # print(self.json_data.keys())
        json_data = self.json_data
        first_key = self.json_data.keys()
        for fkey in first_key:
            redata = {}
            redata[fkey] = {}
            second_key = list(json_data[fkey].keys())
            for skey in second_key:
                redata[fkey][skey] = list(json_data[fkey][skey].keys())
            
            # 전처리 데이터 파일 저장
            json_file_path = f'{fkey.replace("/","_")}.json'
            with open(json_file_path, 'w', encoding='utf-8') as f:
                json.dump(redata, f, ensure_ascii=False, indent=4) 


# 사용 예제
if __name__ == "__main__":
    
    # JSON 데이터
    full_file_path = os.path.join("doc","categories.json")
    with open(full_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 시각화 실행
    visualizer = CategoriesData(data)
    visualizer.test()
