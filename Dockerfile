FROM python:3.10.1-slim

WORKDIR /code

COPY . .
RUN pip install -r requirements.txt


EXPOSE $PORT
CMD [ "python", "app.py"]

