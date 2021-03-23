FROM ubuntu:16.04

LABEL maintainer shvprkatta@gmail.com
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev


WORKDIR /deploy/

#Upgrade pip3 library
# RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /deploy/
# COPY ./requirements.txt /deploy/
# COPY ./iris_trained_model.pkl /deploy/

EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["app.py"]