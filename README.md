# Fundamentus
Esta é uma pequena API feita em python3 para análise de ações da BOVESPA utilizando o site fundamentus (www.fundamentus.com.br), que retorna os 
principais indicadores fundamentalistas em formato JSON.
A API utiliza o microframework Flask.
Também é possível utilizar via linha de comando.

# Website local
Basta executar o arquivo index.html no navegador local com as seguintes flags:
```sh
--disable-web-security --user-data-dir
```

Como por exemplo:
```sh
chromium-browser --disable-web-security --user-data-dir --incognito
```

# Linha de comando
    $ python3 fundamentus.py

# API
Execute o server.py e conecte no endereço (ex.: http://127.0.0.1:5000/) com seu browser

# Requirements
    Flask
    lxml
