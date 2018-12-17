FROM nginx:alpine

RUN mkdir /etc/nginx/sites-available/
RUN mkdir /etc/nginx/sites-enabled/
COPY conf/flask_project /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project

RUN apk add --update --no-cache python3 py-pip
USER root
WORKDIR /src/rfwebui/

COPY . /
RUN pip3 install -r /requirements.pip

#ENTRYPOINT gunicorn --bind 0.0.0.0:8000 wsgi:app