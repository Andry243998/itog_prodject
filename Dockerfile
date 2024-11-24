FROM python:3.9

WORKDIR /usr/src/app

RUN pip install psycopg2-binary

COPY . .

CMD ["python", "./app.py"]
