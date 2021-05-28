# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /application
COPY ./docker/python/requirements.txt /application/
RUN pip install -r requirements.txt
#COPY . /application/
#ENTRYPOINT ["./docker/python/docker-entrypoint.sh"]

ADD ./docker/python/docker-entrypoint.sh /usr/bin/docker-entrypoint
RUN chmod +x /usr/bin/docker-entrypoint
#RUN sed -i -e 's/\r$//' /usr/bin/docker-entrypoint

ENTRYPOINT ["docker-entrypoint"]
