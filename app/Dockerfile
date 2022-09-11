FROM python:3.9-buster

WORKDIR /test

ENV PYTHONPATH /test

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
RUN ls

CMD ["./entrypoint.sh"]