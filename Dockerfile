# https://github.com/komljen/dockerfile-examples/blob/master/ubuntu/Dockerfile
FROM continuumio/miniconda3

RUN apt-get update

RUN apt-get -y install \
            build-essential \
            python-dev

RUN apt-get -y install \
          vim \
          htop \
          unzip \
          curl \
          git-core

RUN pip install --upgrade pip

# Install useful tools for interactive debugging
RUN pip install ipython ipdb

# Copy project over to docker
ADD . /code

# Install project and dependencies
RUN python /code/setup.py develop 
RUN pip install -r /code/requirements.txt

EXPOSE 6544

# Run server
CMD ["/code/scripts/start.sh"]
