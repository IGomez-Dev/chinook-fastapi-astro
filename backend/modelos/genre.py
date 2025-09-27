from sqlmodel import SQLModel

class GenreBase(SQLModel):
  Name: str

class GenreCreate(GenreBase):
  pass

class GenreUpdate(SQLModel):
  Name: str | None = None
