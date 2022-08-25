
FROM python:3.9

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./app /api/app

CMD gunicorn -b 0.0.0.0:80 -w 4 -k uvicorn.workers.UvicornWorker app.main:app