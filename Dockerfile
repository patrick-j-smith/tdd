FROM python:3.14-slim

LABEL authors="patrick-smith"

COPY src /src

WORKDIR /src

CMD ["python", "manage.py", "runserver"]