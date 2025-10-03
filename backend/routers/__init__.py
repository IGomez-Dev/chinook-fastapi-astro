from .album_router import router as album_router
from .artist_router import router as artist_router
from .customer_router import router as customer_router
from .employee_router import router as employee_router
from .genre_router import router as genre_router
from .invoice_line_router import router as invoice_line_router
from .invoice_router import router as invoice_router
from .media_type_router import router as media_type_router
from .playlist_track_router import router as playlist_track_router
from .playlist_router import router as playlist_router
from .track_router import router as track_router

__all__ = [
  'album_router',
  'artist_router',
  'customer_router',
  'employee_router',
  'genre_router',
  'invoice_line_router',
  'invoice_router',
  'media_type_router',
  'playlist_track_router',
  'playlist_router',
  'track_router'
]