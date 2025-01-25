from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.common.keys import Keys
from urllib.parse import quote


import random

from fake_useragent import UserAgent

import time
import json


class CategoryScraper:
    def __init__(self):
        # 크롬 옵션 설정
        self.chrome_options = Options()

        self.chrome_options.add_argument(
            "--headless"
        )  # Headless 모드 활성화 (백그라운드 실행)
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )
        self.chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-logging"]
        )
        # 쿠팡 관련 헤더 및 쿠키 추가
        self.chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        )
        # 쿠키 세션을 유지하기 위한 설정 (필요한 쿠키를 추가)
        self.chrome_options.add_argument(
            "cookie=PCID=10282413319922033681825; _fbp=fb.1.1732540395592.383498674480525198; \
                MARKETID=10282413319922033681825; sid=212d43a0427646268355415f23ff3be0e5d29075; \
                x-coupang-origin-region=KOREA; x-coupang-target-market=KR; x-coupang-accept-language=ko_KR;"
        )

        # 드라이버 설정
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=self.chrome_options,
        )

        self.categories = {}

    async def get_coupang_category(self, item_name):
        encoded_item_name = quote(item_name)
        coupang_url = f"https://www.coupang.com/np/search?component=&q={encoded_item_name}&channel=user"
        self.url = coupang_url

        try:
            # 페이지 로드
            self.driver.get(self.url)
            time.sleep(2)
            # ul 태그 안의 첫 번째 li 요소 가져오기
            ul_element = self.driver.find_element(By.ID, "productList")
            first_li = ul_element.find_element(By.TAG_NAME, "li")  # 첫 번째 li 요소

            # li 안의 링크(a 태그) 가져오기
            link = first_li.find_element(By.TAG_NAME, "a")
            href = link.get_attribute("href")

            time.sleep(2)

            self.driver.get(href)
            # # 링크로 이동 전에 잠시 대기 (혹은 페이지가 완전히 로드될 때까지 대기)
            time.sleep(3)
            # ID가 breadcrumb인 ul 태그를 찾음
            breadcrumb_ul = self.driver.find_element(By.ID, "breadcrumb")

            # ul 안의 모든 li 태그 찾기
            li_elements = breadcrumb_ul.find_elements(By.TAG_NAME, "li")

            # li 태그에서 텍스트 추출
            breadcrumb_texts = ">".join(
                [li.text.strip() for li in li_elements if li.text.strip()][1:]
            )

        except Exception as e:
            print(e)
            print(f"오류 발생: 최상위 함수에서 메세지")

        finally:
            self.driver.quit()
            return {"href": href, "category": breadcrumb_texts}

    def scrape_categories(self):
        """
        카테고리를 계층적으로 탐색하여 JSON 구조 생성
        """
        self.url = "https://datalab.naver.com/shoppingInsight/sCategory.naver"
        try:
            # 페이지 로드
            self.driver.get(self.url)
            time.sleep(2)

            # 첫 번째 set_period category를 타겟팅
            set_period = self.driver.find_elements(
                By.CSS_SELECTOR, "div.set_period.category"
            )[0]
            self.driver.execute_script(
                "arguments[0].className += ' target_category';", set_period
            )  # 고유 클래스 추가

            # 1분류 드롭다운 선택
            first_select = set_period.find_element(By.CSS_SELECTOR, "div.select")
            first_select.click()
            time.sleep(1)

            # 1분류 요소 수집
            first_categories = first_select.find_elements(
                By.CSS_SELECTOR, "ul.select_list.scroll_cst li a.option"
            )

            for first_category in first_categories:
                first_name = first_category.get_attribute("text").strip()
                first_cid = first_category.get_attribute("data-cid")

                # 1분류 클릭
                first_category.click()
                time.sleep(1)

                # 2분류 수집
                self.categories[first_name] = self.get_subcategories(set_period, 2)

                # 1분류 다시 열기
                first_select.click()
                time.sleep(1)

            # JSON 저장
            with open("categories.json", "w", encoding="utf-8") as f:
                json.dump(self.categories, f, ensure_ascii=False, indent=4)

        except Exception as e:
            print(f"오류 발생: 최상위 함수에서 메세지")

        finally:
            self.driver.quit()

    def get_subcategories(self, set_period, level):
        """
        현재 분류 단계에서 하위 카테고리 수집
        """
        subcategories = {}
        try:
            # 고유 클래스를 부여받은 특정 드롭다운 선택
            current_select = set_period.find_element(
                By.CSS_SELECTOR, f"div.select:nth-of-type({level})"
            )
            current_select.click()  # 드롭다운 열기
            time.sleep(1)

            # print(f"--- {level}분류 드롭다운 ---")
            # print(current_select)
            # print("-------------------------")

            # 현재 드롭다운 내부의 하위 카테고리 수집
            subcategory_elements = current_select.find_elements(
                By.CSS_SELECTOR, "ul.select_list.scroll_cst li a.option"
            )

            if not subcategory_elements:  # 하위 카테고리가 없으면 종료
                print(f"{level}분류에서 하위 카테고리 없음")
                return {}

            for subcategory in subcategory_elements:
                sub_name = subcategory.get_attribute("text").strip()
                sub_cid = subcategory.get_attribute("data-cid")

                # 하위 카테고리 클릭
                subcategory.click()
                time.sleep(1)

                # 3분류 클릭 후 4분류가 동적으로 추가되는 경우 처리
                if level == 3:
                    try:
                        div_select_checker = set_period.find_elements(
                            By.CSS_SELECTOR, f"div.select"
                        )
                        if len(div_select_checker) == 4:
                            # 4분류 리스트 수집
                            subcategories[sub_name] = self.get_4th_level_categories(
                                set_period
                            )
                        else:
                            subcategories[sub_name] = {}
                    except Exception as e:
                        print(f"4분류 추가 실패 또는 존재하지 않음")
                        subcategories[sub_name] = {}
                elif level < 3:  # 최대 3분류까지만 재귀 호출
                    subcategories[sub_name] = self.get_subcategories(
                        set_period, level + 1
                    )

                # 현재 레벨 드롭다운 다시 열기
                current_select.click()
                time.sleep(1)
        except Exception as e:
            print(f"{level}분류 수집 중 오류 발생")

        return subcategories

    def get_4th_level_categories(self, set_period):
        """
        4분류의 카테고리를 리스트 형태로 수집
        """
        categories = []
        try:

            # 4분류 드롭다운 요소 선택
            fourth_select = set_period.find_element(
                By.CSS_SELECTOR, f"div.select:nth-of-type({4})"
            )
            fourth_select.click()  # 드롭다운 열기
            time.sleep(1)
            # 4분류 리스트 수집
            category_elements = fourth_select.find_elements(
                By.CSS_SELECTOR, "ul.select_list.scroll_cst li a.option"
            )
            for category in category_elements:
                categories.append(category.get_attribute("text").strip())
        except Exception as e:
            print(f"4분류 수집 중 오류 발생 함수메세지")

        return categories


def main():
    scraper = CategoryScraper()
    scraper.get_coupang_category()


if __name__ == "__main__":
    main()
