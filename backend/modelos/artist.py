from sqlmodel import SQLModel

class ArtistBase(SQLModel):
  Name: str

class ArtistCreate(ArtistBase):
  pass

class ArtistUpdate(ArtistBase):
  Name: str | None = None
