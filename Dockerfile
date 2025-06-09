FROM us.gcr.io/broad-dsp-gcr-public/terra-jupyter-python:1.1.6

USER root
ENV PIP_USER= 
ENV VENV_PATH=/home/jupyter/py39_venv

RUN apt-get update && \
    apt-get install -y software-properties-common git && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.9 python3.9-venv python3.9-dev curl && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9 && \
    python3.9 -m venv $VENV_PATH && \
    $VENV_PATH/bin/pip install --upgrade pip && \
    $VENV_PATH/bin/pip install pandas==1.3.1 cchardet && \
    $VENV_PATH/bin/pip install git+https://github.com/carrollaboratory/ftd-omop-validator.git && \
    chown -R jupyter:jupyter $VENV_PATH && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER jupyter
