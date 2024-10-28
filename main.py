from bs4 import BeautifulSoup
import requests
import time

root = 'https://subslikescript.com'

target_ulr = f'{root}/movies_letter-A'
response = requests.get(target_ulr)
soup = BeautifulSoup(response.text, 'lxml')

pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

for page in range(1, 6):
    response = requests.get(f'{target_ulr}?page={page}')
    soup = BeautifulSoup(response.text, 'lxml')

    box = soup.find('article', class_='main-article')
    ulrs = [ulr['href'] for ulr in box.find_all('a', href=True)]

    for ulr in ulrs:
        try:
            response = requests.get(f'{root}{ulr}')
            soup = BeautifulSoup(response.text, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').text
            transcript = box.find('div', class_='full-script').get_text(separator=' ', strip=True)

            time.sleep(1)

            with open(f'{title}.txt', 'a', encoding='utf-8') as file:
                file.write(transcript)
        except:
            print(f'-----Link not working-----')
    
        
    
