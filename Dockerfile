FROM python:4.0
WORKDIR /usr/ecommerce/backend
ADD . /usr/ecommerce/backend
RUN pip install -r requirements/base.txt