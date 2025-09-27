from sqlmodel import SQLModel

class MediaTypeBase(SQLModel):
  Name: str

class MediaTypeCreate(MediaTypeBase):
 pass

class MediaTypeUpdate(SQLModel):
  Name: str | None = None