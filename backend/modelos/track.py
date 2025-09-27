from sqlmodel import SQLModel

class TrackBase(SQLModel):
  Name: str
  Composer: str | None = None
  Milliseconds: int
  Bytes: int
  UnitPrice: float

class TrackCreate(TrackBase):
  AlbumId: int
  MediaTypeId: int
  GenreId: int

class TrackUpdate(SQLModel):
  Name: str | None = None
  Composer: str | None = None
  Milliseconds: int | None = None
  Bytes: int | None = None
  UnitPrice: float | None = None
  AlbumId: int | None = None
  MediaTypeId: int | None = None
  GenreId: int | None = None