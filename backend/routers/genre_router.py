from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from database import get_session
from modelos import Genre, GenreCreate, GenreUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/genres', tags=['genres'])

session_dep = Annotated[Session, Depends(get_session)]


@router.post('/', response_class=Genre, status_code=201)
def create_genre(genre_data: GenreCreate, session: session_dep):
  db_genre = Genre.model_validate(genre_data)
  return create_item(session, db_genre)


@router.get('/', response_class=list[Genre])
def read_genres(session: session_dep):
  return get_all_items(session, Genre)


@router.get('/{genre_id}', response_model=Genre)
def read_genre(genre_id: int, session: session_dep):
  genre = get_item_by_id(session, Genre, genre_id)
  if not genre:
    raise HTTPException(
      status_code=404,
      detail='Genre no encontrado'
    )
  return genre


@router.put('/{genre_id}', response_model=Genre)
def update_genre(genre_id: int, session: session_dep, genre_data: GenreUpdate):
  db_genre = get_item_by_id(session, Genre, genre_id)
  if not db_genre:
    raise HTTPException(
      status_code=404,
      detail='Genre no encontrado'
    )
  genre_update = update_item(session, db_genre, genre_data.model_dump(exclude_unset=True))
  return genre_update


@router.delete('/{genre_id}', status_code=204)
def delete_genre(genre_id: int, session: session_dep):
  db_genre = get_item_by_id(session, Genre, genre_id)
  if not db_genre:
    raise HTTPException(
      status_code=404,
      detail='Genre no encontrado'
    )
  delete_item(session, db_genre)
  return