FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi==2021.3.4
RUN pip install joblib==1.1.0
RUN pip install pandas==1.2.3
RUN pip install git+https://github.com/ersilia-os/lazy-qsar.git@e2e6a504815c107558ee12f194c057ddb3c56198
RUN pip install xgboost==1.6.2

WORKDIR /repo
COPY . /repo
