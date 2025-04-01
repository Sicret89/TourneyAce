FROM python:3.13.2-bookworm AS dev

COPY ../ .
RUN pip install -r requirements-dev.txt

WORKDIR /src

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=70", "--reload"]
