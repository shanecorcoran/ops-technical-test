FROM python:2.7-alpine3.9

COPY /app /app
WORKDIR /app

RUN apt-get update python -y && pip install -r requirements.txt

CMD ["python app.py"]