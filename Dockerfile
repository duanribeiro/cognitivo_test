FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get install -y python-pip python-dev python-psycopg2 postgresql-client

# Set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the current directory contents into the container
ADD . /app/
RUN pip install -r requirements.txt
RUN cat run.sh

CMD ["./run.sh"]