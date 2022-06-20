FROM alpine:latest

RUN apk --update add bash py-pip py3-magic py3-openssl openssl 

ENV STATIC_PATH /var/www/html/fundamentus/

COPY ./required.txt /var/www/html/
RUN pip install --upgrade pip
RUN pip install -r /var/www/html/required.txt

#Copy api files
COPY ./*.py /var/www/html/

#Garbage collector
RUN rm -rf /var/www/html/requirements.txt

EXPOSE 5000
WORKDIR /var/www/html
ENTRYPOINT ["python3", "server.py"]
