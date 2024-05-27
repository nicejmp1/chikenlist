import requests as req
from bs4 import BeautifulSoup as bs
import json
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")
folder_path = "gamachiChicken"
filename = f"{folder_path}/gamachiChicken_{current_date}.json"

def get_menu_data(url, base_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    soup = bs(res.text, "lxml")

    menu = soup.select(".gall_con a.list_tit")
    sub = soup.select(".gall_con .gall_text_href > p")
    menuimage = soup.select(".gall_href > a > img")

    menu_data = []
    for menu, sub, menuimage in zip(menu, sub, menuimage):
        menuimage = menuimage['src'].strip()

        if menuimage.startswith('/'):
            menuimage = base_url + menuimage

        menu_data.append({
            'Menutitle': menu.text.strip(),
            'Subtitle': sub.text.strip(),
            'menuimage': menuimage
        })

    return menu_data

tab_urls = [
    "https://www.gamachi.co.kr/b/menu&sca=%EC%B9%98%ED%82%A8%EB%A9%94%EB%89%B4",
    "https://www.gamachi.co.kr/b/menu&sca=%EC%82%AC%EC%9D%B4%EB%93%9C%EB%A9%94%EB%89%B4",
]
base_url = "https://www.gamachi.co.kr"
all_tabs_data = []

for tab_url in tab_urls:
    menu_data = get_menu_data(tab_url, base_url)
    all_tabs_data.extend(menu_data)

# 데이터 추출 및 저장
all_tabs_data.extend(menu_data)

# JSON 파일로 저장
with open(filename, "w", encoding='utf-8') as f:
    json.dump(all_tabs_data, f, ensure_ascii=False, indent=4)


print(f"메뉴 데이터를 {filename} 파일에 저장했습니다.")
