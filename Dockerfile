FROM python:3.6-alpine3.10
LABEL AUTHOR="Ajil Raju <ajilraju01@gmail.com>"
WORKDIR /usr/src/app
COPY ./src/ .
CMD [ "python", "./game.py" ]
