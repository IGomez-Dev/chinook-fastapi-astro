from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Playlist, PlaylistCreate, PlaylistUpdate
from crud import *
from typing import Annotated

router = APIRouter(prefix='/playlists', tag=['playlists'])

session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=Playlist, status_code=status.HTTP_202_CREATED)
async def create_playlist(playlist_data: PlaylistCreate, session: session_dep):
  playlist = Playlist(**playlist_data.model_dump)
  return await create_item(session, playlist)

@router.get('/', response_model=list[Playlist])
async def read_playlists(session: session_dep):
  return await get_all_items(session, Playlist)

@router.get('/{playlist_id}', response_model=Playlist)
async def read_playlist(playlist_id: int, session:session_dep):
  playlist = await get_item_by_id(session, Playlist, playlist_id)
  if not playlist:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Playlist no encontrado'
    )
  return playlist

@router.put('/{playlist_id}', response_model=Playlist)
async def update_playlist(playlist_id: int, playlist_model: PlaylistUpdate,session: session_dep):
  playlist = await get_item_by_id(session, Playlist, playlist_id)
  if not playlist:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Playlist no encontrado'
    )
  up_playlist = await update_item(session, playlist, playlist_model.model_dump(exclude_unset=True))
  return up_playlist

@router.delete('/{playlist_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_playlist(playlist_id: int, session:session_dep):
  playlist = await get_item_by_id(session, Playlist, playlist_id)
  if not playlist:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Playlist no encontrado'
    )
  await delete_item(session, playlist)
  return