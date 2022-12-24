FROM python:latest

ADD main.py /app/
ADD submodules.py /app/
ADD secret_token.py /app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

WORKDIR /app/
