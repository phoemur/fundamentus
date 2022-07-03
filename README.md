# Fundamentus
Esta é uma pequena API feita em python3 para análise de ações da BOVESPA utilizando o site fundamentus (www.fundamentus.com.br), que retorna os principais indicadores fundamentalistas em formato JSON. A API utiliza o microframework Flask. Também é possível utilizar via linha de comando.

## instalação:
* pip3 install -r app/requirements.txt

## Executando na linha de comando
### Ações 
* python3 app/fundamentus.py
### FII
* python3 app/fundamentusfii.py

## Iniciando a API
Execute o _python3 app/app.py_ e conecte no endereço a baixo com seu browser

* http://127.0.0.1:8080/


## Acessando as melhores ações e fundos imobiliários
Aqui voce pode colocar um valor menor ou igual a 100, como segue o exemplo

* http://127.0.0.1/acoes/10
* http://127.0.0.1/fii/10

## Acessando as APIs
* http://127.0.0.1/api/acoes/fundamentus.json
* http://127.0.0.1/api/fii/fundamentus.json

## Health check
* http://127.0.0.1/health

## Docker app
* podman build -t fundamentus:v1 .
* podman run -it --rm --name fundamentus_app -p 8080:8080 fundamentus:v1

## Deploy openshift
[Comandos openshift](https://github.com/laurobmb/fundamentus/blob/master/openshift.comandos.md)