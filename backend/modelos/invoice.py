from sqlmodel import SQLModel, Field
from datetime import datetime

class InvoiceBase(SQLModel):
  InvoiceDate: datetime
  BillingAddress: str
  BillingCity: str
  BillingState: str | None = Field(default=None)
  BillingCountry: str
  BillingPostalCode: str | None = None
  Total: float


class InvoiceCreate(InvoiceBase):
  CustomerId: int


class InvoiceUpdate(SQLModel):
  CustomerId: int | None = None
  InvoiceDate: datetime | None = None
  BillingAddress: str | None = None
  BillingCity: str | None = None
  BillingState: str | None = None
  BillingCountry: str | None = None
  BillingPostalCode: str | None = None
  Total: float | None = None