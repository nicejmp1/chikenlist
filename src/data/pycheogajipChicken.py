from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import os
import time
from datetime import datetime

# URL 목록
urls = [
    "https://www.cheogajip.co.kr/bbs/board.php?bo_table=allmenu&page=1",
    "https://www.cheogajip.co.kr/bbs/board.php?bo_table=allmenu&page=2"
]

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
folder_path = "cheogajipChicken"
filename = f"{folder_path}/cheogajipChicken_{current_date}.json"
base_url = "https://www.cheogajip.co.kr"

# 폴더가 없으면 생성
os.makedirs(folder_path, exist_ok=True)

# 웹드라이버 설정
options = ChromeOptions()
options.add_argument('--headless')  # GUI 없이 헤드리스 모드로 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

# 암시적 대기 시간 추가
browser.implicitly_wait(10)

def clean_sub_text(text):
    """sub 문자열을 정리"""
    return text.replace('\n', ' ').replace('\"', '').replace('\'', '').strip()

def get_menu_data(browser, base_url):
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    menu_data = []
    menu_items = soup.select(".gall_li")
    for item in menu_items:
        title_element = item.select_one('.gall_text_href')
        if title_element:
            title_full_text = title_element.text.strip()
            title = title_full_text.split('\n')[0]
            title = ' '.join(title.split())
        else:
            title = 'No Title'

        sub_element = item.select_one('p')
        sub = clean_sub_text(sub_element.text.strip()) if sub_element else 'No Sub'

        money_element = item.select_one('.menuprice')
        money = money_element.get_text(strip=True) if money_element else 'No Price'

        image_element = item.select_one('.gall_href > img')
        image = image_element['src'] if image_element else 'No Image'
        if image.startswith('/'):
            image = base_url + image

        menu_data.append({
            "title": title,
            "sub": sub,
            "money": money,
            "imageURL": image
        })
    return menu_data


all_menu_data = []

for url in urls:
    browser.get(url)
    try:
        # 대기 시간 증가
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "bo_gall"))
        )
        menu_data = get_menu_data(browser, base_url)
        all_menu_data.extend(menu_data)
        time.sleep(2)  # 간단한 대기 시간 추가
    except Exception as e:
        print(f"Error occurred while fetching data from {url}: {e}")

# 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(all_menu_data, f, ensure_ascii=False, indent=4)

browser.quit()
print(f"메뉴 데이터를 {filename} 파일에 저장했습니다.")
