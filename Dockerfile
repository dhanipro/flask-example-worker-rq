FROM python:3.7-alpine

WORKDIR /app 

COPY requirements.txt .

RUN pip3 install -r requirements.txt 

COPY . .

# ENTRYPOINT ["python3"] 

# CMD ["run.py"]