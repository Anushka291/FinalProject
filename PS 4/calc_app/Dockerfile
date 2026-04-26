FROM python:3.11 

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3002

CMD ["python", "app.py"]