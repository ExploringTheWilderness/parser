from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omgtu.ru/ecab/persons/index.php?b=8'
    page = requests.get(url, verify=False)

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        divs = soup.find('div', id='pagecontent').find_all('div', recursive=False)
        ve = [div.get_text().strip() for div in divs if div.get_text().strip().startswith("И")]

        for name in ve:
            print(name)

        with open('test.txt', 'w', encoding='utf-8') as file:
            for name in ve:
                file.write(name + "\n")
    else:
        print("Ошибка загрузки страницы:", page.status_code)

parse()