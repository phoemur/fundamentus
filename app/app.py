#!/usr/bin/env python3

from flask import Flask, jsonify, render_template, Request
from fundamentus import get_data
from datetime import datetime
import json
from create_cvs_acoes import analise_acoes 
from create_cvs_acoes import check_file_acoes 
from create_cvs_fii import analise_fii 
from create_cvs_fii import check_file_fii

app = Flask(__name__)

# First update
lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
lista = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in lista.items()}


@app.route("/",methods=['GET'])
def fundamentus():
    check_file_acoes()
    check_file_fii()
    acoes = analise_acoes(5)
    fii = analise_fii(5)
    return  render_template('index.html',tables=[acoes.to_html(),fii.to_html()],titles = ['na'])


@app.route("/health",methods=['GET'])
def health():
    data = {'api': 'up'}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/acoes/<page_id>",methods=['GET'])
def melhoresacoes(page_id):
    try:
        page_id = int(page_id)
    except ValueError as e:
        print(e)
        return render_template('error.html')

    if page_id <= 100:
        check_file_acoes()
        anlise = analise_acoes(page_id)
        return render_template('view_acoes.html',tables=[anlise.to_html()],titles = ['na'])
    else:
        return render_template('error.html')


@app.route("/fii/<page_id>",methods=['GET'])
def melhoresfii(page_id):
    try:
        page_id = int(page_id)
    except ValueError as e:
        print(e)
        return render_template('error.html')

    if page_id <= 100:
        check_file_fii()
        anlise = analise_fii(page_id)
        return render_template('table_fii.html',tables=[anlise.to_html()],titles = ['na'])
    else:
        return render_template('error.html')


@app.route("/api/fundamentus.json",methods=['GET'])
def json_api():
    global lista, dia    
    if dia == datetime.strftime(datetime.today(), '%d'):
        return jsonify(lista)
    else:
        lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
        lista = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in lista.items()}
        return jsonify(lista)

app.run(host='0.0.0.0',debug=True,port=8080)
