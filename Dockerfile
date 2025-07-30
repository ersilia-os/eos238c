FROM bentoml/model-server:0.11.0-py311
MAINTAINER ersilia

RUN pip install git+https://github.com/ersilia-os/lazy-qsar.git@main#egg=lazyqsar[descriptors]

WORKDIR /repo
COPY . /repo
