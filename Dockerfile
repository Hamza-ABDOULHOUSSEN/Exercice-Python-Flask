FROM python:3-alpine3.15

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN apk update
RUN apk add --virtual build-deps gcc python3-dev musl-dev
RUN apk add --no-cache mariadb-dev
RUN pip install -r requirements.txt

ENV FLASK_APP app.py
ENV FLASK_DEBUG 1
ENV FLASK_RUN_PORT 5000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]


