from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI(
    title="Currency Converter API",
    description="A simple API to convert amounts between predefined currencies.",
    version="1.0.0"
)

class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    DZD = "DZD"
    GBP = "GBP"
    AED = "AED"

class ConversionRequest(BaseModel):
    amount: float = Field(..., gt=0, description="The amount to convert")
    from_currency: Currency
    to_currency: Currency

EXCHANGE_RATES = {
    Currency.USD: 1.0,
    Currency.EUR: 0.92,
    Currency.DZD: 134.0,
    Currency.GBP: 0.79,
    Currency.AED: 3.67,
}

@app.post("/convert")
async def convert_currency(request: ConversionRequest):
    amount_in_usd = request.amount / EXCHANGE_RATES[request.from_currency]
    converted_amount = amount_in_usd * EXCHANGE_RATES[request.to_currency]

    return {
        "amount": request.amount,
        "from_currency": request.from_currency,
        "to_currency": request.to_currency,
        "converted_amount": round(converted_amount, 2),
        "rate": round(EXCHANGE_RATES[request.to_currency] / EXCHANGE_RATES[request.from_currency], 4)
    }
