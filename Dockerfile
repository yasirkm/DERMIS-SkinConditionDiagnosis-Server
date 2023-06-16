FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

ENV DB-HOST='localhost'
ENV DB-NAME='dermis-db'
ENV DB-CONNECTOR='/cloudsql/connector'

EXPOSE 8080
CMD ["python", "app.py"]