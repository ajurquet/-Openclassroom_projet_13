FROM python:latest

COPY requirements.txt .

RUN pip install -r requirements.txt \
 && mkdir /OC-lettings

COPY . /OC-lettings/

WORKDIR /OC-lettings/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]