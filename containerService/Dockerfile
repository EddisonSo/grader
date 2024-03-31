FROM python:3.9.17-bullseye 

RUN pip install --upgrade pip

COPY ./containerService /opt/containerService
WORKDIR /opt/containerService
RUN pip install -r requirements.txt

WORKDIR /opt/containerService
CMD ["python3", "-u", "container_server.py"]


