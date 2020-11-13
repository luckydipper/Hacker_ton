from bs4 import BeautifulSoup
from pprint import pprint
import requests
import json

html = requests.get('https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&oquery=%EB%82%A0%EC%94%A8&tqi=UIIAFdprvTVss5DeeBwssssstG0-002822&acq=%EC%BD%94%EB%A1%9C%EB%82%98&acr=1&qdt=0')
soup = BeautifulSoup(html.text, 'html.parser')

data1 = soup.find('div', {'class':'status_today'})

data2 = data1.findAll('li')
today_status_1 = data1.find('em',{'class':'info_num'}).text

print('오늘의 국내 확진자: '+today_status_1)

corona_info_dict = {'국내 확진자':today_status_1}
def toJson(corona_info_dict):
    with open('weather.json', 'w', encoding='utf-8') as file :
        json.dump(corona_info_dict, file, ensure_ascii=False, indent='\t')

toJson(corona_info_dict)

