FROM python:latest

COPY requirements.txt .

ENV SENTRY_URL https://9a86db70ddfb4f9aa4bcd5f8ebc6aa98@o1100916.ingest.sentry.io/6126428
ENV SECRET_KEY fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s
ENV DATABASE_URL=sqlite:///db/oc-lettings-site.sqlite3
ENV SQLITE_URL=sqlite:///db/oc-lettings-site.sqlite3

RUN pip install -r requirements.txt \
 && mkdir /OC-lettings \
 && apt-get update

COPY . /OC-lettings/

WORKDIR /OC-lettings/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]