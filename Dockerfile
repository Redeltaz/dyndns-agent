FROM python:3.9-slim

WORKDIR /dyndns

COPY . /dyndns

RUN pip3 install -r requirements.txt

RUN mkdir /var/log/dyndns
RUN touch /var/log/dyndns/agent.log

CMD ["python3", "main.py"]
