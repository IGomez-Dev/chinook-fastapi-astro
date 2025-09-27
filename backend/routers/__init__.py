from .album_router import router as album_router
from .artist_router import router as artist_router
from .customer_router import router as customer_router
from .employee_router import router as employee_router
from .genre_router import router as genre_router

__all__ = [
  'album_router',
  'artist_router',
  'customer_router',
  'employee_router',
  'genre_router',
]