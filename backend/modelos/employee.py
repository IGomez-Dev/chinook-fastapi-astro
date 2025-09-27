from sqlmodel import SQLModel
from datetime import datetime

class EmployeeBase(SQLModel):
  LastName: str
  FirstName: str
  Email: str
    
  Title: str | None = None
  BirthDate: datetime | None = None
  HireDate: datetime | None = None
  Address: str | None = None
  City: str | None = None
  State: str | None = None
  Country: str | None = None
  PostalCode: str | None = None
  Phone: str | None = None
  Fax: str | None = None

class EmployeeCreate(EmployeeBase):
  ReportsTo: int | None = None

class EmployeeUpdate(SQLModel):
  LastName: str | None = None
  FirstName: str | None = None
  Email: str | None = None
    
  Title: str | None = None
  BirthDate: datetime | None = None
  HireDate: datetime | None = None
  Address: str | None = None
  City: str | None = None
  State: str | None = None
  Country: str | None = None
  PostalCode: str | None = None
  Phone: str | None = None
  Fax: str | None = None
    
  ReportsTo: int | None = None