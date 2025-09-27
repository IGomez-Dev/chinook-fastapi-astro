from sqlmodel import SQLModel

class PlaylistBase(SQLModel):
  Name: str

class PlaylistCreate(PlaylistBase):
  pass

class PlaylistUpdate(SQLModel):
  Name: str | None = None
