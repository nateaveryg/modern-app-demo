FROM python:3.10-slim

COPY ./be/requirements.txt ./

RUN pip install --upgrade pip

RUN pip install keyring

RUN pip install keyrings.google-artifactregistry-auth

RUN keyring --list-backends

COPY ./be/.pypirc $HOME/.pypirc

COPY ./be/pip.conf $HOME/.pip/pip.conf

RUN pip install --no-cache-dir -r requirements.txt

COPY ./be/main.py /main.py

ENTRYPOINT [ "python", "main.py" ]