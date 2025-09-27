from sqlmodel import Field, Relationship
from typing import List, Optional
from .artist import ArtistBase
from .album import AlbumBase
from .track import TrackBase
from .playlist_track import PlaylistTrackBase
from .playlist import PlaylistBase
from .media_type import MediaTypeBase
from .genre import GenreBase
from .invoice_line import InvoiceLineBase
from .invoice import InvoiceBase
from .customer import CustomerBase
from .employee import EmployeeBase


class Artist(ArtistBase, table=True):
  ArtistId: int | None = Field(default=None, primary_key=True)

  albums: List['Album'] = Relationship(back_populates='artist')


class Album(AlbumBase, table=True):
  AlbumId: int | None = Field(default=None, primary_key=True)

  ArtistId: int = Field(foreign_key='artist.ArtistId')

  artist: Optional['Artist'] = Relationship(back_populates='albums')
  tracks: List['Track'] = Relationship(back_populates='album')


class Track(TrackBase, table=True):
  TrackId: int | None = Field(default=None, primary_key=True)
  
  AlbumId: int = Field(foreign_key='album.AlbumId')
  MediaTypeId: int = Field(foreign_key='mediatype.MediaTypeId')
  GenreId: int = Field(foreign_key='genre.GenreId')

  album: Optional['Album'] = Relationship(back_populates='tracks')
  media_type: Optional['MediaType'] = Relationship(back_populates='tracks')
  genre: Optional['Genre'] = Relationship(back_populates='tracks')
  playlist_tracks: List['PlaylistTrack'] = Relationship(back_populates='track')     
  invoice_lines: List['InvoiceLine'] = Relationship(back_populates='track')


class PlaylistTrack(PlaylistTrackBase, table=True):
  PlaylistId: int | None = Field(foreign_key='playlist.PlaylistId', primary_key=True)
  TrackId: int | None = Field(foreign_key='track.TrackId', primary_key=True)

  playlist: Optional['Playlist'] = Relationship(back_populates='playlist_tracks')
  track: Optional['Track'] = Relationship(back_populates='playlist_tracks')


class Playlist(PlaylistBase, table=True):
  PlaylistId: int | None = Field(default=None ,primary_key=True)

  playlist_tracks: List['PlaylistTrack'] = Relationship(back_populates='playlist') 


class MediaType(MediaTypeBase, table=True):
  MediaTypeId: int | None = Field(default=None, primary_key=True)

  tracks: List['Track'] = Relationship(back_populates='media_type')


class Genre(GenreBase, table=True):
  GenreId: int | None = Field(default=None, primary_key=True)

  tracks: List['Track'] = Relationship(back_populates='genre')


class InvoiceLine(InvoiceLineBase, table=True):
  InvoiceLineId: int | None = Field(default=None, primary_key=True)

  InvoiceId: int = Field(foreign_key='invoice.InvoiceId')
  TrackId: int = Field(foreign_key='track.TrackId')

  track: Optional['Track'] = Relationship(back_populates='invoice_lines')
  invoice: Optional['Invoice'] = Relationship(back_populates='invoice_lines')


class Invoice(InvoiceBase, table=True):
  InvoiceId: int | None = Field(default=None, primary_key=True)

  CustomerId: int = Field(foreign_key='customer.CustomerId')

  invoice_lines: List['InvoiceLine'] = Relationship(back_populates='invoice')
  customer: Optional['Customer'] = Relationship(back_populates='invoices')


class Customer(CustomerBase, table=True):
  CustomerId: int | None = Field(default=None, primary_key=True)

  SupportRepId: Optional[int] = Field(foreign_key='employee.EmployeeId')

  invoices: List['Invoice'] = Relationship(back_populates='customer')
  employee: Optional['Employee'] = Relationship(back_populates='customers')


class Employee(EmployeeBase, table=True):
  EmployeeId: int | None = Field(default=None, primary_key=True)
    
    # Clave Foránea de auto-referencia para el jefe (ReportsTo)
  ReportsTo: Optional[int] = Field(default=None, foreign_key="employee.EmployeeId")

    # Relación de clientes (Employee es el SupportRep)
  customers: List['Customer'] = Relationship(back_populates='employee')
    
    # Relación de Jefatura (recursiva)
  manager: Optional['Employee'] = Relationship(
    back_populates='subordinates',
    sa_relationship_kwargs={"remote_side": "Employee.EmployeeId"}
  )
  subordinates: List['Employee'] = Relationship(back_populates='manager')