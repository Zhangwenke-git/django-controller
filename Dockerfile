FROM python:3.10
RUN mkdir -p /django
WORKDIR /django
COPY pip.conf /root/.pip/pip.conf
COPY requirements.txt /django
RUN pip install -r /django/requirements.txt
RUN rm -rf /django
COPY . /django
CMD [ "python", "./manage.py", "makemigrations"]
CMD [ "python", "./manage.py", "migrate"]
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:9091"]