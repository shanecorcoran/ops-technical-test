FROM python:2.7-alpine3.9

COPY /app /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]