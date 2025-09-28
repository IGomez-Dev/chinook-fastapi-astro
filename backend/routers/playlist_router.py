from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Playlist, PlaylistCreate, PlaylistUpdate
from crud import *
from typing import Annotated

router = APIRouter(prefix='/playlists', tag=['playlists'])

session_dep = Annotated[AsyncSession, Depends(get_session)]
