# Fundamentus
Esta é uma pequena API feita em python3 para análise de ações da BOVESPA utilizando o site fundamentus (www.fundamentus.com.br), que retorna os principais indicadores fundamentalistas em formato JSON. A API utiliza o microframework Flask. Também é possível utilizar via linha de comando.

## Requirements
    Flask
    lxml
    
## Install with:
    $ pip3 install -r app/requirements.txt

## Linha de comando
    $ python3 app/fundamentus.py

## API
Execute o app.py e conecte no endereço (ex.: http://127.0.0.1:8080/) com seu browser

    $ python3 app/app.py

## Health check

http://127.0.0.1/health

## Melhores ações e fundos imobiliários

Aqui voce pode colocar um valor menor ou igual a 100, como segue o exemplo

http://127.0.0.1/acoes/10
http://127.0.0.1/fii/10