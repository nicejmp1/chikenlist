import os
import requests as req
from bs4 import BeautifulSoup as bs
import json
from datetime import datetime

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
folder_path = "barunChicken"
filename = f"{folder_path}/barunChicken_{current_date}.json"

# 폴더가 존재하지 않을 경우 생성
os.makedirs(folder_path, exist_ok=True)

def get_menu_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    soup = bs(res.text, "lxml")
    menu = soup.select("div.tit")
    sub = soup.select("span.detail_txt")
    price = soup.select("div.price")
    chart_data = []
    for m, s, p in zip(menu, sub, price):
        chart_data.append({
            'Menu': m.text.strip(),
            'Sub': s.text.strip(),
            "Price": p.text.strip(),
        })
    return chart_data

# URL 정의
url = "https://m.booking.naver.com/order/bizes/1090294/items/5720885?theme=place&refererCode=menutab&area=pll"
chart_data = get_menu_data(url)

# 데이터를 JSON 파일로 저장
with open(filename, "w", encoding='utf-8') as f:
    json.dump(chart_data, f, ensure_ascii=False, indent=4)

print(f"메뉴 데이터를 {filename} 파일에 저장했습니다.")
