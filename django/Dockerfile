FROM python:3
WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD [ "python", "manage.py", "runserver", "0.0.0.0:80" ]