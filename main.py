from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from enum import Enum
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, async_session_maker, Base
from models import ConversionHistory

app = FastAPI(
    title="Currency Converter API",
    description="A simple API to convert amounts between predefined currencies and store history.",
    version="1.1.0"
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

# إنشاء الجداول عند بدء التشغيل
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# دالة للحصول على جلسة قاعدة البيانات
async def get_db():
    async with async_session_maker() as session:
        yield session

@app.post("/convert")
async def convert_currency(
    request: ConversionRequest,
    db: AsyncSession = Depends(get_db)
):
    amount_in_usd = request.amount / EXCHANGE_RATES[request.from_currency]
    converted_amount = amount_in_usd * EXCHANGE_RATES[request.to_currency]
    rate = EXCHANGE_RATES[request.to_currency] / EXCHANGE_RATES[request.from_currency]

    # حفظ العملية في قاعدة البيانات
    history = ConversionHistory(
        amount=request.amount,
        from_currency=request.from_currency.value,
        to_currency=request.to_currency.value,
        converted_amount=round(converted_amount, 2),
        rate=round(rate, 4)
    )
    db.add(history)
    await db.commit()
    await db.refresh(history)

    return {
        "id": history.id,
        "amount": request.amount,
        "from_currency": request.from_currency.value,
        "to_currency": request.to_currency.value,
        "converted_amount": round(converted_amount, 2),
        "rate": round(rate, 4)
    }