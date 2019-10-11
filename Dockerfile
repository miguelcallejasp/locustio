FROM python:3.6-alpine3.9

COPY run.sh /

RUN    apk --no-cache add --virtual=.build-dep build-base \
    && apk --no-cache add zeromq-dev \
    && pip install --no-cache-dir locustio==0.10.0 \
    && apk del .build-dep \
    && chmod +x /run.sh \
    && mkdir /locust
WORKDIR /locust
EXPOSE 8089 5557 5558

ENTRYPOINT ["/run.sh"]
