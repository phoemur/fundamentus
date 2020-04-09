#!/usr/bin/env python3

import os
from flask import Flask, jsonify
from fundamentus import get_data
from datetime import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


# First update
lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
lista = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in lista.items()}

@app.route("/")
def json_api():
    global lista, dia
    
    # Then only update once a day
    if dia == datetime.strftime(datetime.today(), '%d'):
        return jsonify(lista)
    else:
        lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
        lista = {outer_k: {inner_k: float(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in lista.items()}
        return jsonify(lista)

port = int(os.environ.get('PORT', 5000))

app.run(debug=True, host='0.0.0.0', port=port) 
