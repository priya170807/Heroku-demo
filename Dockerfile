FROM python:3.8-slim

LABEL maintainer shvprkatta@gmail.com
# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev


WORKDIR /deploy/

#Upgrade pip3 library
# RUN pip3 install --upgrade pip
COPY . /deploy/
RUN pip install -r requirements.txt
# COPY ./requirements.txt /deploy/
# COPY ./iris_trained_model.pkl /deploy/

EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["app.py"]