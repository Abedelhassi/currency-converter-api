# Currency Converter API

A simple FastAPI application to convert amounts between predefined currencies.

## Features
- POST /convert endpoint
- Supports USD, EUR, DZD, GBP, AED
- Uses Pydantic for validation and Enum for currency codes
- Interactive Swagger docs at /docs

## Run locally
pip install fastapi uvicorn[standard]
uvicorn main:app --reload# currency-converter-api
## Run with Docker
docker build -t currency-api .
docker run -d -p 8000:8000 --name currency-container currency-api
Then open http://127.0.0.1:8000/docs
