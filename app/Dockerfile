FROM python:3.8-slim-buster

WORKDIR /opt/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /opt/app

COPY gunicorn.conf.py ./

WORKDIR /opt/app/src
COPY src ./

CMD ["gunicorn", "app:app", "-c", "/opt/app/gunicorn.conf.py"]
