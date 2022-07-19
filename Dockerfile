FROM ubuntu:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN apt update && apt-get upgrade -y
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow
RUN apt-get install -y tzdata
RUN apt install wget unzip zip -y
RUN apt install imagemagick -y

RUN apt install python3-pip -y
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install -y python3-numpy python3-pydot python3-matplotlib python3-opencv python3-graphviz python3-toolz

RUN wget https://github.com/bipinkrish/Colorize-Positive-Bot/releases/download/Model/model.zip && unzip model.zip && rm model.zip
RUN wget https://github.com/bipinkrish/Colorize-Positive-Bot/releases/download/Model/deoldify.zip && unzip deoldify.zip && rm deoldify.zip

CMD ["python3","bot.py"]
