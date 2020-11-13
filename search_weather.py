from bs4 import BeautifulSoup
from pprint import pprint
import requests
import json

html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8')
# pprint(html.text)
soup = BeautifulSoup(html.text, 'html.parser')

data1 = soup.find('div', {'class':'api_subject_bx'})
find_address = data1.find('span', {'class':'btn_select'}).text
Location = '현재 위치: '+find_address

find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
Temperature ='현재 온도: '+find_currenttemp+'℃'

data2 = data1.findAll('dd')
find_dust = data2[0].find('span', {'class':'num'}).text
find_ultra_dust = data2[1].find('span', {'class':'num'}).text
find_ozone = data2[2].find('span', {'class':'num'}).text
dust = '현재 미세먼지: ' +find_dust

ultra_dust = '현재 초미세먼지: '+find_ultra_dust
ozone = '현재 오존지수: '+find_ozone
All = Location + ', ' + Temperature + ', ' + dust + ', ' + ultra_dust + ', ' + ozone
print(All)
#weather_dict = {'위치':find_address,'온도':find_currenttemp,'미세먼지':find_dust, '초미세먼지': find_ultra_dust,'오존지수':find_ozone}


weather_dict = {'tag':"weather",
                "patterns":["What's the weather like today?",
                            "How's the weather today?",
                            "Weather"],
                "responses":All}
print(weather_dict)


def toJson(weather_dict):
    with open('weather.json', 'w', encoding='utf-8') as file :
        json.dump(weather_dict, file, ensure_ascii=False, indent='\t')

toJson(weather_dict)

