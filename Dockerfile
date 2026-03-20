FROM python:3.14-slim

LABEL authors="patrick-smith"

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install "django<6"
RUN pip install "python-decouple"

COPY src /src
COPY ".env" ".env"

WORKDIR /src

CMD ["python", "manage.py", "migrate", "--noinput"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]