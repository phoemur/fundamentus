# Fundamentus
Esta é uma pequena API feita em python3 para análise de ações da BOVESPA utilizando o site fundamentus (www.fundamentus.com.br), que retorna os principais indicadores fundamentalistas em formato JSON. A API utiliza o microframework Flask. Também é possível utilizar via linha de comando.

## Etapas

0. [X] Efetuar web scrapingg na página da fundamentus para obter ações da bolsa brasileira
1. [X] Excluir empresas com EBIT negativo
2. [X] Excluir empresas com EBITDA negativo
4. [0] Excluir empresas em recuperação judicial
5. [X] Criar ranking por Dividend yield, P/VP, P/L
6. [X] Gerar csv a partir dos dados processados
7. [X] Mostra Dividend yield maior que 6%
8. [X] Evita Earning Yield negativo e maior que 10%
9. [X] Evita PL negativo e maior que 4
10. [X] Evita ROE negativo e maior que 80%

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

* http://127.0.0.1:8080/acoes/10
* http://127.0.0.1:8080/fii/10

## Acessando as APIs
* http://127.0.0.1:8080/api/acoes/fundamentus.json
* http://127.0.0.1:8080/api/fii/fundamentus.json

## Health check
* http://127.0.0.1:8080/health

## Docker app
* podman build -t fundamentus:v1 .
* podman run -it --rm --name fundamentus_app -p 8080:8080 fundamentus:v1

## Deploy openshift
[Comandos openshift](https://github.com/laurobmb/fundamentus/blob/master/openshift.comandos.md)
