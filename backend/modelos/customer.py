from sqlmodel import SQLModel

class CustomerBase(SQLModel):
  FirstName: str
  LastName: str
  Company: str | None = None
  Address: str
  City: str
  State: str | None = None
  Country: str
  PostalCode: str | None = None
  Phone: str | None = None
  Fax: str | None = None
  Email: str

class CustomerCreate(CustomerBase):
  SupportRepId: int

class CustomerUpdate(SQLModel):
  FirstName: str | None = None
  LastName: str | None = None
  Company: str | None = None
  Address: str | None = None
  City: str | None = None
  State: str | None = None
  Country: str | None = None
  PostalCode: str | None = None
  Phone: str | None = None
  Fax: str | None = None
  Email: str | None = None
