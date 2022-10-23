# DynDNS Agent

Agent that act like a Dynamic DNS by using OVH API

## Installation
Before starting, you need to prepare the log file 
```bash
sudo mkdir /var/log/dyndns
sudo touch /var/log/dyndns/agent.log
```
And then fill the [.env.example](.env.example) file with your own OVH credentials and use this command :
```bash
mv .env.example .env
```

### With Docker
To launch the agent with docker, first build the image
```
docker build -t dyndns-agent .
```
And then launch the container 
```
docker run -d --name=dyndns-agent --restart=always -v /var/log/dyndns:/var/log/dyndns dyndns-agent:latest
```

### Without Docker
To launch without docker, first install all the dependencies 
```
pip3 install -r requirements.txt
```
And then launch the agent
```
python3 main.py
```

#### Logs
All the logs of the agent (launched with docker or not) will be written in `/var/log/dyndns/agent.log` and will show whether the domain has been changed or not
