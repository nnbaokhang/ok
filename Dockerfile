FROM python:3.5-alpine

RUN apk add --update \
    supervisor \
    patch \
    ca-certificates \
    nginx \
    perl \
    musl-dev \
    openssl-dev \
    libffi-dev \
    python-dev \
    gcc


RUN mkdir /code
WORKDIR /code
COPY . /code
 
RUN pip3 --timeout=60 install --no-cache-dir -r requirements.txt

EXPOSE 5000
RUN cd /code 
CMD ["python","manage.py","createdb"]
CMD ["python","manage.py","server"]
