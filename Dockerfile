FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y ffmpeg \
 && pip install -r requirements.txt

CMD ["gunicorn", "-b", ":8080", "app:app"]
