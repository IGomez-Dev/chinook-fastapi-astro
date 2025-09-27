from sqlmodel import SQLModel

class PlaylistTrackBase(SQLModel):
  pass

class PlaylistTrackCreate(PlaylistTrackBase):
  PlaylistId: int
  TrackId: int

class PlaylistTrackUpdate(SQLModel):
  PlaylistId: int | None = None
  TrackId: int | None = None