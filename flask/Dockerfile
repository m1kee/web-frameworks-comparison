FROM python:3

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV FLASK_APP=wsgi.py
ENV FLASK_DEBUG=False

CMD [ "gunicorn", "--bind", "0.0.0.0:80", "wsgi:app" ]