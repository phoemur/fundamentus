#!/usr/bin/env python3

import re
import urllib.request
import urllib.parse
import http.cookiejar

from lxml.html import fragment_fromstring
from collections import OrderedDict
from decimal import Decimal

def todecimal(string):
  try:
    string = string.replace('.', '')
    string = string.replace(',', '.')
  except:
    string = 'sem valor'
    pass

  try:
    if (string.endswith('%')):
      string = string[:-1]
      return Decimal(string) / 100
    else:
      return Decimal(string)
  except:
    return string


def get_data_fii(*args, **kwargs):
    url = 'http://www.fundamentus.com.br/fii_resultado.php'
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'),
                         ('Accept', 'text/html, text/plain, text/css, text/sgml, */*;q=0.01')]

    # Aqui estão os parâmetros de busca das ações
    # Estão em branco para que retorne todas as disponíveis
    data = {'ffo_y_min': '',
            'ffo_y_max': '',
            'divy_min': '',
            'divy_max': '',
            'pvp_min': '',
            'pvp_max' : '',
            'mk_cap_min': '',
            'mk_cap_max': '',
            'qtd_imoveis_min': '',
            'qtd_imoveis_max': '',
            'preco_m2_min': '',
            'preco_m2_max': '',
            'aluguel_m2_min': '',
            'aluguel_m2_max': '',
            'cap_rate_min': '',
            'cap_rate_max': '',
            'vacancia_min': '',
            'vacancia_max': '',
            'segmento': '',
            'negociada': 'ON',
            'ordem': '1',
            'x': '28',
            'y': '16'}

    with opener.open(url, urllib.parse.urlencode(data).encode('UTF-8')) as link:
        content = link.read().decode('ISO-8859-1')
        #print(content)

    pattern = re.compile('<table id="tabelaResultado".*</table>', re.DOTALL)
    content = re.findall(pattern, content)[0]
    page = fragment_fromstring(content)
    result = OrderedDict()

    for rows in page.xpath('tbody')[0].findall("tr"):
        result.update({rows.getchildren()[0][0].getchildren()[0].text: {
          'Segmento': todecimal(rows.getchildren()[1].text),
          'Cotacao': todecimal(rows.getchildren()[2].text),
          'FFOYield': todecimal(rows.getchildren()[3].text),
          'DY': todecimal(rows.getchildren()[4].text),
          'P/VP': todecimal(rows.getchildren()[5].text),
          'LIQUIDEZ': todecimal(rows.getchildren()[6].text),
          'VALORMERCADO': todecimal(rows.getchildren()[7].text),
          'QTDIMAVEIS': todecimal(rows.getchildren()[8].text),
          'PM2': todecimal(rows.getchildren()[9].text),
          'AM2': todecimal(rows.getchildren()[10].text),
          'CAPRATE': todecimal(rows.getchildren()[11].text),
          'VACANCIA': todecimal(rows.getchildren()[12].text)}})

    return result
    

if __name__ == '__main__':
    from waitingbar import WaitingBar
    
    #progress_bar = WaitingBar('[*] Downloading...')
    result = get_data_fii()
    #progress_bar.stop()

    result_format = '{0:<10} {1:<20} {2:<10} {3:<15} {4:<10} {5:<7} {6:<15} {7:<15} {8:<15} {9:<15} {10:<15} {11:<7}'
    print(result_format.format(
      'Papel',
      'Segmento',
      'Cotacao',
      'FFOYield',
      'DY',
      'P/VP',
      'LIQUIDEZ',
      'VALORMERCADO',
      'QTDIMAVEIS',
      'PM2',
      'AM2',
      'CAPRATE',
      'VACANCIA'))

    print('-' * 190)
    for key, value in result.items():
      print(result_format.format(key,
        value['Segmento'],
        value['Cotacao'],
        value['FFOYield'],
        value['DY'],
        value['P/VP'],
        value['LIQUIDEZ'],
        value['VALORMERCADO'],
        value['QTDIMAVEIS'],
        value['PM2'],
        value['AM2'],
        value['CAPRATE'],
        value['VACANCIA']))
