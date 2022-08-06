FROM python:3.9.13

WORKDIR /usr/scr/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# EXPOSE 8000

# CMD ["gunicorn", "--bind", "0:8000", "config.wsgi:application"]