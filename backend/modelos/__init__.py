from .modelos_db import Artist, Album, Customer, Track, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track

from .album import AlbumCreate, AlbumUpdate
from .artist import ArtistCreate, ArtistUpdate
from .customer import CustomerCreate, CustomerUpdate
from .employee import EmployeeCreate, EmployeeUpdate
from .genre import GenreCreate, GenreUpdate
from .invoice import InvoiceCreate, InvoiceUpdate
from .invoice_line import InvoiceLineCreate, InvoiceLineUpdate
from .media_type import MediaTypeCreate, MediaTypeUpdate
from .playlist_track import PlaylistTrackCreate, PlaylistTrackUpdate
from .playlist import PlaylistCreate, PlaylistUpdate
from .track import TrackCreate, TrackUpdate