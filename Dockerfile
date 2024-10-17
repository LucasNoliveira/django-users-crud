FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
COPY .env /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
