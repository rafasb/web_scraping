import asyncio
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from time import sleep

async def get_soup(url: str = 'https://www.loteriasyapuestas.es/es/loteria-nacional'):
    session = AsyncHTMLSession()
    try:
        response = await session.get(url)
        sleep(3)
        await response.html.arender()  # Aquí es donde necesitas usar await
        html = response.html.raw_html.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        with open('loteria_nacional_2.html', 'w') as f:
            f.write(html)
    finally:
        await session.close()
    return soup

def get_premios(soup: BeautifulSoup) -> list[str]:
    divs = soup.find_all('div', class_='c-resultado-lnac__premio')
    return [div.text for div in divs]

def get_reintegros(soup: BeautifulSoup) -> list[str]:
    ul = soup.find('ul', class_='c-resultado-lnac__reintegros')
    if ul is None:
        return []
    lis = ul.find_all('li')
    return [li.text.replace('R','') for li in lis]


if __name__ == '__main__':
    url = 'https://www.loteriasyapuestas.es/es/loteria-nacional'

    soup = asyncio.run(get_soup(url))

    for premio in get_premios(soup):
        print(premio)
        
    print('------------------')
    print('Reintegros')

    print(get_reintegros(soup))