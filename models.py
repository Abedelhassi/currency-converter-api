from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class ConversionHistory(Base):
    __tablename__ = "conversion_history"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    from_currency = Column(String, nullable=False)
    to_currency = Column(String, nullable=False)
    converted_amount = Column(Float, nullable=False)
    rate = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Conversion {self.amount} {self.from_currency} -> {self.to_currency}>"
