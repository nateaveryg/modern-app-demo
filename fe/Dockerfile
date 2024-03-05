FROM python:3.10-slim

COPY ./fe/requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY ./fe/* ./

ENTRYPOINT [ "python", "main.py" ]