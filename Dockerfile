FROM python:3-alpine

COPY requirements.txt /tmp

WORKDIR /tmp

RUN pip3 install --upgrade pip && \
     pip3 install virtualenv && \
     pip3 install --upgrade jsonpatch && \
    pip3 install --no-cache-dir -r requirements.txt 



CMD ["python"]