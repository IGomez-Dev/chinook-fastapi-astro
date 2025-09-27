from sqlmodel import SQLModel

class AlbumBase(SQLModel):
  Title: str

class AlbumCreate(AlbumBase):
  ArtistId: int

class AlbumUpdate(SQLModel):
  Title: str | None = None
  ArtistId: int | None = None
