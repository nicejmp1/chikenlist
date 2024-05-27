from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime

urls = [
    "https://www.mexicana.co.kr/menu/product.asp?page=1&CateCode=1000001&searchstr=",
    "https://www.mexicana.co.kr/menu/product.asp?page=2&CateCode=1000001&searchstr=",
    "https://www.mexicana.co.kr/menu/product.asp?page=3&CateCode=1000001&searchstr=",
    "https://www.mexicana.co.kr/menu/product.asp?page=4&CateCode=1000001&searchstr=",
    "https://www.mexicana.co.kr/menu/product.asp?catecode=1000002",
    "https://www.mexicana.co.kr/menu/product.asp?page=2&CateCode=1000002&searchstr="
]

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
folder_path = "mexicanaChicken"
filename = f"{folder_path}/mexicanaChicken_{current_date}.json"
base_url = "https://www.mexicana.co.kr/"


# 웹드라이버 설정
options = ChromeOptions()
options.add_argument('--headless')  # GUI 없이 헤드리스 모드로 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

# try:
#     more_button = WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, ".paging_all"))
#     )
#     if more_button:
#         browser.execute_script("paging>.num>a[0].click();", more_button)
#         print("Clicked '더보기' button.")
#         time.sleep(3)
# except Exception as e:
#     print("Error clicking '더보기':", e)

time.sleep(3)

def get_menu_data(browser, base_url):
    
    html_source_updated = browser.page_source
    soup = BeautifulSoup(html_source_updated, 'html.parser')

    menu_data = []
    menu = soup.select(".mt30 > ul > li")

    for chicken in menu:
        title = chicken.select_one(".tit dt").text.strip()
        subtitle = chicken.select_one(".tit dd").text.strip()
        money = chicken.select_one(".money strong").text.strip()
        image = chicken.select_one("img").get('src')
        if image.startswith('/'):
            image = base_url + image

        menu_data.append({
            "Title": title,
            "Subtitle": subtitle,
            "Money" : money,
            "imageURL": image
        })
    return menu_data

all_menu_data = []

for url in urls:
    browser.get(url)
# 페이지가 완전히 로드될 때까지 대기
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menuArea"))
    )

    menu_data = get_menu_data(browser, base_url)
    all_menu_data.extend(menu_data)
    time.sleep(3)

# 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(all_menu_data, f, ensure_ascii=False, indent=4)

# 브라우저 종료
browser.quit()

print(f"메뉴 데이터를 {filename} 파일에 저장했습니다.")
