# Fundamentus

This is a simple Python3 API to help analysing BOVESPA stocks, it collects data (scraping) from the Fundamentus website (www.fundamentus.com.br), which contains important "fundamental indicators", and return it as JSON.

This API uses the Flask microframework, but it can also be used directly on command line.

## Development env setup

Install the dependencies:

`$ pip3 install -r requirements.txt`

## Command line usage

`$ python3 fundamentus.py`

## HTTP API

### Development API

`$ python3 server.py`

After starting the server, access the <http://127.0.0.1:5000/> URL on your browser.

### Production API

`$ gunicorn server:app`

After starting the server, access the <http://127.0.0.1:8000/> URL on your browser.

## Production deploy

You can easily deploy this API to production, using [Heroku](https://www.heroku.com/):

### Heroku initial setup

* First, you need to install the Heroku CLI, if you haven't yet: <https://devcenter.heroku.com/articles/heroku-cli>
* Then, you need to login to it `$ heroku login`
* Lastly, you need to create a heroku app `$ heroku create your-api-name-here`

### Deploy

You can deploy to heroku, with:

* `$ git push heroku master`

In case you are in a different branch, ex `develop`, you can deploy with:

* `$ git push heroku develop:master`

After deploying to heroku, you can access the API on <http://your-api-name-here.herokuapp.com/>

### Production troubleshooting

In case the production API on Heroku fails, you can visualize the logs with this command:

`$ heroku logs --tail`
