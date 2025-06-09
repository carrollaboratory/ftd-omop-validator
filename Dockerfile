FROM us.gcr.io/broad-dsp-gcr-public/terra-jupyter-python:1.1.6

USER root
ENV PIP_USER= 

# Install Python 3.9 and create venv
RUN apt-get update && \
    apt-get install -y software-properties-common git && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.9 python3.9-venv python3.9-dev curl && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9 && \
    python3.9 -m venv /opt/py39_venv && \
    echo "venv creation: done" && \
    /opt/py39_venv/bin/pip install --upgrade pip && \
    /opt/py39_venv/bin/pip install pandas==1.3.1 && \
    echo "pandas installation: done" && \
    /opt/py39_venv/bin/pip install cchardet && \
    echo "install cchadet: done" && \
    /opt/py39_venv/bin/pip install git+https://github.com/carrollaboratory/ftd-omop-validator.git && \
    echo "install pandas: done" && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER jupyter
