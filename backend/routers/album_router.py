from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Album, AlbumCreate, AlbumUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/albums', tags=['albums'])

session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=Album, status_code=status.HTTP_201_CREATED)
async def create_album(album_data: AlbumCreate, session: session_dep):
  db_album = Album(**album_data.model_dump())
  return await create_item(session, db_album)


@router.get("/", response_model=list[Album])
async def read_albums(session: session_dep):
  return await get_all_items(session, Album)


@router.get('/{album_id}', response_model=Album)
async def read_album(album_id: int, session: session_dep):
  album = await get_item_by_id(session, Album, album_id)
  if not album:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Álbum no encontrado'
    )
  return album


@router.put('/{album_id}', response_model=Album)
async def update_album(album_id: int, album_data: AlbumUpdate, session: session_dep):
  db_album = await get_item_by_id(session, Album, album_id)
  if not db_album:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Álbum no encontrado'
    )
  update = await update_item(session, db_album, album_data.model_dump(exclude_unset=True))
  return update


@router.delete('/{album_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_album(album_id: int, session: session_dep):
  db_album = await get_item_by_id(session, Album, album_id)
  if not db_album:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Álbum no encontrado'
    )
  await delete_item(session, db_album)
  return
