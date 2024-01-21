# Leer páginas web

Este es solo un ejemplo de como leer páginas web. En este caso, se ha usado la página web de [Loterías y Apuestas del Estado]

Resulta totalmente prescindible el uso de web scraping para obtener los datos de la página web, ya que la página web contiene llamadas a una API REST con los verbos GET donde se puede obtener la información de una forma más sencilla en formato JSON. No obstante, el ejemplo sirve para ver y comparar como se puede leer una página web dinámica frente a leer una página web estática.

## HTML estático.

Es muy sencillo ya que en la primera respuesta del servidor se obtiene el código HTML de la página web. Por lo tanto, solo es necesario hacer una petición HTTP y obtener el código HTML para despues parsearlo con alguna librería como BeautifulSoup.

El resultado se puede ver en el script scrap_1.py

## HTML dinámico.

En este caso, el servidor no devuelve el código HTML de la página web, sino que devuelve tanto el código HTML como el código JavaScript. Por lo tanto, es necesario ejecutar el código JavaScript para obtener el código HTML final. Tras las dificultades de usar Selenium, se ha optado por usar la librería [requests-html]

El resultado se puede ver en el script scrap_2.py

## Pre-requisitos (Linux)

El problema de Selenium es que requiere de un navegador web para funcionar. Por lo tanto, es necesario instalar un navegador web en el servidor

