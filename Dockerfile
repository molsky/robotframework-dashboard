FROM nginx:alpine

RUN apk add --update --no-cache python3 py-pip nano
RUN mkdir /etc/nginx/sites-available/
RUN mkdir /etc/nginx/sites-enabled/
RUN mkdir /usr/robotdashboard

COPY conf/flask_project /etc/nginx/sites-available/
COPY requirements.pip /

RUN pip3 install -r /requirements.pip
RUN ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project

USER root
WORKDIR /usr/work/rfwebui/

ENTRYPOINT gunicorn --bind 0.0.0.0:8000 wsgi:app