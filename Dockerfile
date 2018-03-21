# https://github.com/komljen/dockerfile-examples/blob/master/ubuntu/Dockerfile
FROM continuumio/miniconda3

RUN \
  apt-get update && \
  apt-get -y install \
          vim \
          htop \
          unzip \
          curl \
          git-core

# Install useful tools for interactive debugging
RUN pip install ipython ipdb
