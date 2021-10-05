FROM python:3
ENV PYTHONUNBUFFERED=1y
WORKDIR /code
COPY ./backend/requirements.txt /code/

RUN pip install -r requirements.txt
COPY ./backend /code/
