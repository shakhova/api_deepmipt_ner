FROM ubuntu:16.04
MAINTAINER vimvim
USER root

RUN apt-get update -y -qq \
  && apt-get install -y software-properties-common \
  && add-apt-repository ppa:jonathonf/python-3.6 \
  && apt-get update --fix-missing \
  && apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv git\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3.6 python \
  && python -m pip install --upgrade pip \
  && python -m pip install git+https://github.com/deepmipt/ner

WORKDIR /usr/src/app
ENV PATH=/usr/src/app:$PATH

COPY requirements.txt ./

RUN python -m pip install --no-cache-dir -r requirements.txt

CMD ["python", "ner_flask.py"]