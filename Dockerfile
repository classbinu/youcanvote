FROM python:3.9.13
WORKDIR /usr/scr/app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0:8000"]