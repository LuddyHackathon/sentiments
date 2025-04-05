FROM python:3.9-slim

RUN mkdir -p /home/python/sentiments

WORKDIR /home/python/sentiments

COPY requirements.txt ./

ENV DEBIAN_FRONTEND=noninteractive

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 65535

ENTRYPOINT [ "python"]

CMD ["app.py"]
