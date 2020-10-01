FROM python:3.8

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY api.py ./

EXPOSE 8080

RUN pip install flask

RUN pip install requests

CMD ["python","api.py"]
