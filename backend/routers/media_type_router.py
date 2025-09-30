from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import MediaType, MediaTypeCreate, MediaTypeUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/media_types', tags=['media_types'])

session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=MediaType, status_code=status.HTTP_201_CREATED)
async def create_media_type(media_type_data: MediaTypeCreate, session: session_dep):
  media_type = MediaType(**media_type_data.model_dump)
  return await create_item(session, media_type)


@router.get('/', response_model= list[MediaType])
async def read_media_types(session: session_dep):
  return await get_all_items(session, MediaType)


@router.get('/{media_type_id}', response_model=MediaType)
async def read_media_type(media_type_id: int, session: session_dep):
  media_type = await get_item_by_id(session, MediaType, media_type_id)
  if not media_type:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Media Type no encontrado'
    )
  return media_type


@router.put('/{media_type_id}', response_model=MediaType)
async def update_media_type(media_type_id:int, media_type_model: MediaTypeUpdate, session: session_dep):
  media_type = await get_item_by_id(session, MediaType, media_type_id)
  if not media_type:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Media Type no encontrado'
    )
  ud_media_type = await update_item(session, media_type, media_type_model.model_dump(exclude_unset=True))
  return ud_media_type


@router.delete('/{media_type_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_media_type(media_type_id: int, session: session_dep):
  media_type = await get_item_by_id(session, MediaType, media_type_id)
  if not media_type:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Media Type no encontrado'
    )
  await delete_item(session, media_type)
  return