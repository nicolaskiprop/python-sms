#start with a base image
FROM ubuntu:16.04
RUN apt-get update && apt-get -y upgrade
#install python
RUN apt-get -y install python && \
    apt-get -y install python-pip && \
    apt-get -y install nano 
#install framework
WORKDIR ussd/
COPY . ussd/
RUN cd ussd/ && pip install -r requirements.txt
EXPOSE 5000:5000
CMD ["python","sms.py"]
