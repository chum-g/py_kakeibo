FROM python:3.10
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
RUN apt update
# nvmのインストールに必要なモノをインストール
RUN apt install -y curl git
SHELL [ "/bin/bash", "-c" ]
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
# lts版のnodeをインストール
RUN . $HOME/.nvm/nvm.sh && \
    nvm install --lts && \
    nvm use --lts && \
    node -v && npm -v && \
    npm i -g yarn && \
    npm i -g vue-cli
    # vue init vuetifyjs/webpack vue_py_kakeibo
COPY . /code/
# RUN python py_kakeibo/manage.py migrate