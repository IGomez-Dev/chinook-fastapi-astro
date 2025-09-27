from sqlmodel import SQLModel

class InvoiceLineBase(SQLModel):
  UnitPrice: float
  Quantity: int
  
class InvoiceLineCreate(InvoiceLineBase):
  InvoiceId: int
  TrackId: int

class InvoiceLineUpdate(SQLModel):
  InvoiceId: int | None = None
  TrackId: int | None = None
  UnitPrice: float | None = None
  Quantity: int | None = None