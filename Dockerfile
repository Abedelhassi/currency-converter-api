FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip setuptools wheel jaraco.context msgpack

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall -y setuptools wheel
COPY main.py .
COPY database.py .
COPY models.py .
COPY static ./static
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]