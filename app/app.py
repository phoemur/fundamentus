#!/usr/bin/env python3

from flask import Flask, jsonify, render_template, Request
from fundamentus import get_data
from datetime import datetime
import json
from create_cvs import analise 
from create_cvs import check_file 

app = Flask(__name__)

# First update
lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
lista = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in lista.items()}

@app.route("/",methods=['GET'])
def fundamentus():
    return '<h1 style="font-weight: bold">Fundamentos API</h1>'

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
def melhores(page_id):
    try:
        page_id = int(page_id)
    except ValueError as e:
        print(e)
        return render_template('error.html')

    if page_id <= 100:
        check_file()
        anlise = analise(page_id)
        return render_template('view.html',tables=[anlise.to_html()],titles = ['na'])
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
