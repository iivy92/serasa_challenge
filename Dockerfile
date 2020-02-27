FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN pip install -r ./requirements/requirements.txt

EXPOSE 80

CMD ["python", "run.py"]