import requests
from bs4 import BeautifulSoup
import fake_headers
import json
from pprint import pprint
from fun import s1

headers_gen = fake_headers.Headers(browser='chrome', os='win')

link = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page=0'
responce = requests.get(link, headers=headers_gen.generate())
print(f'Status code: {responce.status_code}')
soup = BeautifulSoup(responce.text, 'lxml')
content = soup.find('div', id='a11y-main-content')
vacancy = content.find_all('div', class_='serp-item')
vac_dict = {}
for _ in vacancy:
    vac = _.find('a', class_='serp-item__title')
    vac_name = vac.text
    link_vac = vac['href']
    responce = requests.get(link_vac, headers=headers_gen.generate())
    soup = BeautifulSoup(responce.text, 'lxml')
    info = soup.find('div', class_='vacancy-branded-user-content')
    if info is None:
        info = soup.find('div', class_='g-user-content')
    if 'Jango' in info.text or 'Flask' in info.text:
        company = soup.find('div', class_='vacancy-company-redesigned')
        company_name = company.find('span', class_='bloko-header-section-2 bloko-header-section-2_lite').text
        if '\xa0' in company_name:
            company_name.replace('\xa0', ' ')
        
        vac_city = company.find('span', {'data-qa': 'vacancy-view-raw-address'})
        if vac_city is None:
            vac_city = company.find('p', {'data-qa': "vacancy-view-location"}).text
        else:
            vac_city = vac_city.text.split(',')[0]
        
        sal = _.find('span', class_="bloko-header-section-2")
        if sal is None:
            sal = 'Не указана'
        else:
            sal = sal.text.replace('\u202f', '')
        
        vac_dict[vac_name] = {'Ссылка': link_vac, 'Зарплата': sal, 'Название компании': company_name, 'Город': vac_city}


if __name__=='__main__':
    with open ('data.json', 'w', encoding='utf-8') as js:
        json.dump(vac_dict, js,ensure_ascii=False, indent=4)

    s1()






