FROM python:3.8.7-buster
COPY ./requirements.txt /home
RUN pip install -r /home/requirements.txt
COPY . /home
WORKDIR /home
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi"]
