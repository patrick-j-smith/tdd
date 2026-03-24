FROM python:3.14-slim

LABEL authors="patrick-smith"

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install "django<6" gunicorn "python-decouple" whitenoise

COPY src /src

WORKDIR /src

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
CMD ["gunicorn", "--bind", ":8888", "superlists.wsgi:application"]