FROM python:2.7-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY ../app/requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY ../app /app
WORKDIR /app
CMD ["python app.py"]