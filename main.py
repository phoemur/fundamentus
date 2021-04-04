from fastapi import FastAPI, HTTPException
from api.fundamentus import get_data
from datetime import datetime

app = FastAPI()

lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
lista = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in lista.items()}


@app.get("/")
def get_all_urls():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list


@app.get("/ticker/{ticker_name}")
def get_ticker(ticker_name: str):
    "Retorna os indicadores da empresa consultada"

    ticker_name = ticker_name.upper()
    if ticker_name not in lista:
        raise HTTPException(status_code=404, detail="Ticker: {} não encontrado!".format(ticker_name))
    return (lista[ticker_name])


@app.get("/tickers")
def get_all_tickers():
    "Retorna os indicadores de todas as empresas cadastradas na Bovespa"

    return lista
