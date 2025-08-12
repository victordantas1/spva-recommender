FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src
COPY ./run.sh .

RUN sed -i 's/\r$//' ./run.sh

RUN chmod +x ./run.sh

CMD ["./run.sh", "prod"]