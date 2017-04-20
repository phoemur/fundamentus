#!/usr/bin/env python3

import re
import urllib.request
import urllib.parse
import http.cookiejar
import time

from lxml.html import fragment_fromstring
from collections import OrderedDict
from firebase import firebase
import json

def get_data(*args, **kwargs):
    url = 'http://www.fundamentus.com.br/resultado.php'
    cj = http.cookiejar.CookieJar() 
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'),
                         ('Accept', 'text/html, text/plain, text/css, text/sgml, */*;q=0.01')]

    # Aqui estão os parâmetros de busca das ações
    # Estão em branco para que retorne todas as disponíveis
    data = {'pl_min':'',
            'pl_max':'',
            'pvp_min':'',
            'pvp_max' :'',
            'psr_min':'',
            'psr_max':'',
            'divy_min':'',
            'divy_max':'',
            'pativos_min':'',
            'pativos_max':'',
            'pcapgiro_min':'',
            'pcapgiro_max':'',
            'pebit_min':'',
            'pebit_max':'',
            'fgrah_min':'',
            'fgrah_max':'',
            'firma_ebit_min':'',
            'firma_ebit_max':'',
            'margemebit_min':'',
            'margemebit_max':'',
            'margemliq_min':'',
            'margemliq_max':'',
            'liqcorr_min':'',
            'liqcorr_max':'',
            'roic_min':'',
            'roic_max':'',
            'roe_min':'',
            'roe_max':'',
            'liq_min':'',
            'liq_max':'',
            'patrim_min':'',
            'patrim_max':'',
            'divbruta_min':'',
            'divbruta_max':'',
            'tx_cresc_rec_min':'',
            'tx_cresc_rec_max':'',
            'setor':'',
            'negociada':'ON',
            'ordem':'1',
            'x':'28',
            'y':'16'}

    with opener.open(url, urllib.parse.urlencode(data).encode('UTF-8')) as link:
        content = link.read().decode('ISO-8859-1')

    pattern = re.compile('<table id="resultado".*</table>', re.DOTALL)
    reg = re.findall(pattern, content)[0]
    page = fragment_fromstring(reg)
    lista = OrderedDict()

    for rows in page.xpath('tbody')[0].findall("tr"):
        lista.update({rows.getchildren()[0][0].getchildren()[0].text: {'cotacao': rows.getchildren()[1].text,
                                                                       'P/L': rows.getchildren()[2].text,
                                                                       'P/VP': rows.getchildren()[3].text,
                                                                       'PSR': rows.getchildren()[4].text,
                                                                       'DY': rows.getchildren()[5].text,
                                                                       'P/Ativo': rows.getchildren()[6].text,
                                                                       'P/Cap.Giro': rows.getchildren()[7].text,
                                                                       'P/EBIT': rows.getchildren()[8].text,
                                                                       'P/Ativ.Circ.Liq.': rows.getchildren()[9].text,
                                                                       'EV/EBIT': rows.getchildren()[10].text,
                                                                       'EBITDA': rows.getchildren()[11].text,
                                                                       'Mrg.Liq.': rows.getchildren()[12].text,
                                                                       'Liq.Corr.': rows.getchildren()[13].text,
                                                                       'ROIC': rows.getchildren()[14].text,
                                                                       'ROE': rows.getchildren()[15].text,
                                                                       'Liq.2m.': rows.getchildren()[16].text,
                                                                       'Pat.Liq': rows.getchildren()[17].text,
                                                                       'Div.Brut/Pat.': rows.getchildren()[18].text,
                                                                       'Cresc.5a': rows.getchildren()[19].text}})
    
    return lista
    
if __name__ == '__main__':
    from waitingbar import WaitingBar
    
    THE_BAR = WaitingBar('[*] Downloading...')
    lista = get_data()
    THE_BAR.stop()

    firebase = firebase.FirebaseApplication('https://bovespastockratings.firebaseio.com/', None)

    file_output = open('firebase.json', 'w')


    #Transform em uma lista, agora preciso passar para formato JSON
    array_format = list(lista.items())

    # Adiciona a data que esta pegando a info
    json_format = {
      "date": time.strftime("%c")
    }

    for i in range(0, len(array_format)): 
      json_format[str(i)] = {
        str(array_format[i][0]):array_format[0][1]
      }

#     json_format = {
#   'DAGB33': {
#      'ROE': '-0,47%',
#      'Liq.Corr.': '1,16',
#      'Liq.2m.': '916.730,00',
#      'EBITDA': '4,75%',
#      'PSR': '0,000',
#      'ROIC': '4,59%',
#      'P/Ativo': '0,000',
#      'Pat.Liq': '9.803.230.000,00',
#      'cotacao': '480,00',
#      'P/EBIT': '0,00',
#      'P/Cap.Giro': '0,00',
#      'DY': '0,00%',
#      'P/VP': '0,00',
#      'Mrg.Liq.': '0,38%',
#      'P/L': '0,00',
#      'P/Ativ.Circ.Liq.': '0,00',
#      'Div.Brut/Pat.': '1,37',
#      'EV/EBIT': '0,00',
#      'Cresc.5a': '46,43%'
#   }
# }

    # new_json = json_format

    # beautify JSON
    new_json = json.dumps(json_format, sort_keys=True, indent=4, separators=(',', ': '))
    # # Write in the file
    file_output.write(new_json)
    file_output.close()


    result = firebase.post('/stocks', data=new_json )
    print (result)
    










    # print('{0:<7} {1:<7} {2:<10} {3:<7} {4:<10} {5:<7} {6:<10} {7:<10} {8:<10} {9:<11} {10:<11} {11:<7} {12:<11} {13:<14} {14:<7}'.format('Papel',
    #                                                                                                                                       'Cotação',
    #                                                                                                                                       'P/L',
    #                                                                                                                                       'P/VP',
    #                                                                                                                                       'PSR',
    #                                                                                                                                       'DY',
    #                                                                                                                                       'P/EBIT',
    #                                                                                                                                       'EV/EBIT',
    #                                                                                                                                       'EBITDA',
    #                                                                                                                                       'Mrg.Liq.',
    #                                                                                                                                       'Liq.Corr.',
    #                                                                                                                                       'ROIC',
    #                                                                                                                                       'ROE',
    #                                                                                                                                       'Div.Brut/Pat.',
    #                                                                                                                                       'Cresc.5a'))
    
    # print('-'*154)
    # for k, v in lista.items():
    #     print('{0:<7} {1:<7} {2:<10} {3:<7} {4:<10} {5:<7} {6:<10} {7:<10} {8:<10} {9:<11} {10:<11} {11:<7} {12:<11} {13:<14} {14:<7}'.format(k,
    #                                                                                                                                           v['cotacao'],
    #                                                                                                                                           v['P/L'],
    #                                                                                                                                           v['P/VP'],
    #                                                                                                                                           v['PSR'],
    #                                                                                                                                           v['DY'],
    #                                                                                                                                           v['P/EBIT'],
    #                                                                                                                                           v['EV/EBIT'],
    #                                                                                                                                           v['EBITDA'],
    #                                                                                                                                           v['Mrg.Liq.'],
    #                                                                                                                                           v['Liq.Corr.'],
    #                                                                                                                                           v['ROIC'],
    #                                                                                                                                           v['ROE'],
    #                                                                                                                                           v['Div.Brut/Pat.'],
    #                                                                                                                                           v['Cresc.5a']))

