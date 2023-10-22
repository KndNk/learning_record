FROM python:3.10.9-slim-buster

WORKDIR /python-app
RUN pip3 install flask

COPY ./app.py /python-app/app.py

EXPOSE 8080
ENTRYPOINT ["python3", "app.py"]