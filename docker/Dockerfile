FROM python:3

RUN mkdir /app
COPY . /
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

CMD ["./run.sh"]