from scrap_2 import get_premios, get_reintegros, get_soup
import asyncio

url = 'https://www.loteriasyapuestas.es/es/loteria-nacional'

soup = asyncio.run(get_soup(url))

for premio in get_premios(soup):
    print(premio)
    
print('------------------')
print('Reintegros')

print(get_reintegros(soup))