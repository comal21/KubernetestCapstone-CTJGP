FROM ubuntu:18.04
LABEL maintainer="Admin CloudThat"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./code /app
CMD [ "python", "./app.py" ]
