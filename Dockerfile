FROM ubuntu:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN apt update && apt-get upgrade -y
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow
RUN apt-get install -y tzdata
RUN apt install wget -y
RUN apt install imagemagick -y

RUN apt install python3-pip -y
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN wget https://github.com/bipinkrish/Colorize-Positive-Bot/releases/download/Model/colorization_release_v2.caffemodel -O model/colorization_release_v2.caffemodel

CMD ["python3","bot.py"]
