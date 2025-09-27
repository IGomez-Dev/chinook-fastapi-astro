from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Artist, ArtistUpdate, ArtistCreate
from crud import create_item, get_item_by_id, get_all_items, update_item, delete_item
from typing import Annotated

router = APIRouter(prefix='/artists', tags=['artists'])

session_dep = Annotated[AsyncSession, Depends(get_session)]

@router.post('/', response_model=Artist, status_code=status.HTTP_201_CREATED)
async def create_artist(artist_data: ArtistCreate, session: session_dep):
    db_artist = Artist.model_validate(artist_data)
    return await create_item(session, db_artist)


@router.get("/", response_model=list[Artist])
async def read_artists(session: session_dep):
    return await get_all_items(session, Artist)


@router.get('/{artist_id}', response_model=Artist)
async def read_artist(artist_id: int, session: session_dep):
    artist = await get_item_by_id(session, Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail='Artist no encontrado')
    return artist


@router.put('/{artist_id}', response_model=Artist)
async def update_artist(artist_id: int, artist_data: ArtistUpdate, session:session_dep):
    db_artist = await get_item_by_id(session, Artist, artist_id)
    if not db_artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Artist no encontrado')
    updated_artist = await update_item(session, db_artist, artist_data.model_dump(exclude_unset=True))
    return updated_artist


@router.delete('/{artist_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_artist(artist_id: int, session: session_dep):
    db_artist = await get_item_by_id(session, Artist, artist_id)
    if not db_artist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Artist no encontrado'
        )
    await delete_item(session, db_artist)
    return