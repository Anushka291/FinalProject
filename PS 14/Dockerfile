FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask selenium

EXPOSE 8004

CMD ["python", "app.py"]