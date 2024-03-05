FROM python:3.10-slim

COPY ./be/requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY ./be/main.py /main.py

ENTRYPOINT [ "python", "main.py" ]