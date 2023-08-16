FROM python:3.11

RUN apt-get update && apt-get install -y redis-server


WORKDIR /app


COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


EXPOSE 7000


CMD ["gunicorn", "-w", "4", "wsgi:app"]
