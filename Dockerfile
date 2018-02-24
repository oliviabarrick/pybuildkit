FROM python:alpine3.6

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . /tmp

RUN cd /tmp && python setup.py install
