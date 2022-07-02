
FROM python:slim
LABEL maintainer="Lauro Gomes <laurobmb@gmail.com>"
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN python -m pip install -r requirements.txt 
EXPOSE 8080
CMD [ "python", "app.py" ]
