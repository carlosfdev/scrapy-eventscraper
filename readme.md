### Instalación

Probado en un venv con Python 3.6

`pip install -r requirements.txt`

### Uso

`scrapy crawl meetup -o output/meetup.json`

Escribe el output en el json, si ya estaba creado sigue, escribiendo al final del fichero, por lo que habría que borrarlo antes, para sucesivas ejecuciones se puede utilizar el siguiente comando

`rm output/meetup.json && scrapy crawl meetup -o output/meetup.json`