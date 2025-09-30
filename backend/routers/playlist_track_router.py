from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import PlaylistTrack, PlaylistTrackCreate, PlaylistTrackUpdate
from crud import *
from typing import Annotated

router = APIRouter(prefix='/playlist_track', tags=['playlist track'])


session_dep = Annotated[AsyncSession, Depends(get_session)]

@router.post('/', response_model=PlaylistTrack, status_code=status.HTTP_201_CREATED)
async def create_playlist_track(playlist_track_data:PlaylistTrackCreate, session: session_dep):
  playlist_track = PlaylistTrack(**playlist_track_data.model_dump)
  return await create_item(session, playlist_track)

@router.get('/', response_model=list[PlaylistTrack])
async def read_playlist_tracks(session: session_dep):
  return await get_all_items(session, PlaylistTrack)

@router.get('/{playlist_track_id}', response_model=PlaylistTrack)
async def read_playlist_track(playlist_track_id: int, session: session_dep):
  playlist_track = await get_item_by_id(session, PlaylistTrack, playlist_track_id)
  if not playlist_track:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Playlist Track no encontrado'
    )
  return playlist_track

@router.put('/{playlist_track_id}', response_model=PlaylistTrack)
async def update_playlist_track(playlist_track_id: int, playlist_track_model: PlaylistTrackUpdate, session: session_dep):
  playlist_track = await get_item_by_id(session, PlaylistTrack, playlist_track_id)
  if not playlist_track:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Playlist Track no encontrado'
    )
  up_playlist_track = await update_item(session, playlist_track, playlist_track_model.model_dump(exclude_unset=True))
  return up_playlist_track

@router.delete('/{playlist_track_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_playlist_track(playlist_track_id: int, session: session_dep):
  playlist_track = await get_item_by_id(session, PlaylistTrack, playlist_track_id)
  if not playlist_track:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Playlist Track no encontrado'
    )
  await delete_item(session, playlist_track)
  return