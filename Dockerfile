FROM python:3.7

COPY ./server /app
WORKDIR /app/

RUN pip install -r requirements.txt

ENV PYTHONPATH=/app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
