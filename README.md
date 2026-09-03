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
