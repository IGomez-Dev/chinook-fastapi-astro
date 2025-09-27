from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Genre, GenreCreate, GenreUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/genres', tags=['genres'])

session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=Genre, status_code=201)
async def create_genre(genre_data: GenreCreate, session: session_dep):
  db_genre = Genre(**genre_data.model_dump())
  return await create_item(session, db_genre)


@router.get('/', response_model=list[Genre])
async def read_genres(session: session_dep):
  return await get_all_items(session, Genre)


@router.get('/{genre_id}', response_model=Genre)
async def read_genre(genre_id: int, session: session_dep):
  genre = await get_item_by_id(session, Genre, genre_id)
  if not genre:
    raise HTTPException(
      status_code=404,
      detail='Genre no encontrado'
    )
  return genre


@router.put('/{genre_id}', response_model=Genre)
async def update_genre(genre_id: int, session: session_dep, genre_data: GenreUpdate):
  db_genre = await get_item_by_id(session, Genre, genre_id)
  if not db_genre:
    raise HTTPException(
      status_code=404,
      detail='Genre no encontrado'
    )
  genre_update = await update_item(session, db_genre, genre_data.model_dump(exclude_unset=True))
  return genre_update


@router.delete('/{genre_id}', status_code=204)
async def delete_genre(genre_id: int, session: session_dep):
  db_genre = await get_item_by_id(session, Genre, genre_id)
  if not db_genre:
    raise HTTPException(
      status_code=404,
      detail='Genre no encontrado'
    )
  await delete_item(session, db_genre)
  return