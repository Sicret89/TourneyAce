FROM python:3.13.2-bookworm AS builder

COPY ../src .
RUN pip install -r requirements.txt

FROM builder AS app

WORKDIR /src
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=70"]