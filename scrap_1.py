import requests
from bs4 import BeautifulSoup

def get_soup(url: str = 'https://www.loteriasyapuestas.es/es/loteria-nacional'):
    # usamos requests para obtener el html
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    with open('loteria_nacional_1.html', 'w') as f:
        f.write(html)
    return soup

def get_premios(soup: BeautifulSoup) -> list[str]:
    divs = soup.find_all('div', class_='c-resultado-lnac__premio')
    return [div.text for div in divs]

def get_reintegros(soup: BeautifulSoup) -> list[str]:
    ul = soup.find('ul', class_='c-resultado-lnac__reintegros')
    lis = ul.find_all('li')
    return [li.text.replace('R','') for li in lis]

url = 'https://www.loteriasyapuestas.es/es/loteria-nacional'

soup = get_soup(url)

for premio in get_premios(soup):
    print(premio)
    
print('------------------')
print('Reintegros')

print(get_reintegros(soup))