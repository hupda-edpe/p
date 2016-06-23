# ProcessMaker Wrapper
## Usage
Build and run Docker image:  
`docker build -t=testcase .`  
`docker run -ti testcase python`

When in interactive Python console, import client functions:  
`from client import *`


## Configuration
Theoretically there can now be more than one configuration for a PM host, although only one config file will be evaluated and it has to be named `config.json`. For future use there could be a subdirectory with named config files or a more elaborate tree in the already existing config file. 

Also, preparations for possible future SSL use by adding a protocol type in config. 

## Conventions
* `act_uid` is immediately renamed `tas_uid`
* `prj_uid` is immediately renamed `pro_uid`

## Next steps
Maybe setup a [Django](https://www.djangoproject.com) in order to be able to have our app function better as a server as well as a client.

###Dockerfile

```docker
FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
```

### requirements.txt
```
Django
psycopg2
```

### docker-compose.yml
```yaml
version: '2'
services:
  db:
    image: postgres
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```
