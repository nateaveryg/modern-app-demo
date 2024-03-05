FROM python:3.10-slim

# COPY ./fe/requirements.txt ./

COPY ./fe* /

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]