FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2021.03.4
RUN pip install joblib==1.1.0
RUN pip install pandas==1.2.3
RUN pip install git+https://github.com/ersilia-os/lazy-qsar.git

WORKDIR /repo
COPY . /repo
