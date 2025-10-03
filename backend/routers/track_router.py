from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Track, TrackCreate, TrackUpdate
from crud import *
from typing import Annotated

router = APIRouter(prefix='/tracks', tags=['tracks'])

session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=Track, status_code=status.HTTP_201_CREATED)
async def create_track(track_data: TrackCreate, session: session_dep):
  track = Track(**track_data.model_dump())
  return await create_item(session, track)

@router.get('/', response_model=list[Track])
async def read_tracks(session: session_dep):
  return await get_all_items(session, Track)

@router.get('/{track_id}', response_model=Track)
async def read_track(track_id: int, session: session_dep):
  track = await get_item_by_id(session, Track, track_id)
  if not track:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Track no encontrado'
    )
  return track

@router.put('/{track_id}', response_model=Track)
async def update_track(track_id: int, track_model: TrackUpdate,session: session_dep):
  track = await get_item_by_id(session, Track, track_id)
  if not track:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Track no encontrado'
    )
  up_track = await update_item(session, track, track_model.model_dump(exclude_unset=True))
  return up_track

@router.delete('/{track_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_track(track_id: int, session: session_dep):
  track = await get_item_by_id(session, Track, track_id)
  if not track:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Track no encontrado'
    )
  await delete_item(session, track)
  return