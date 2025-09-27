from sqlmodel import select, SQLModel
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type, TypeVar


ModelType = TypeVar('ModelType', bound=SQLModel)


async def create_item(session: AsyncSession, item: ModelType):
  session.add(item)
  await session.commit()
  await session.refresh(item)
  return item


async def get_item_by_id(session: AsyncSession, model: Type[ModelType], item_id:int):
  return await session.get(model, item_id)


async def get_all_items(session: AsyncSession, model: Type[ModelType]):
  result = await session.execute(select(model))
  return result.scalars().all()


async def update_item(session: AsyncSession, item: ModelType, data: dict):
  for key, value in data.items():
    setattr(item, key, value)
  session.add(item)
  await session.commit()
  await session.refresh(item)
  return item


async def delete_item(session: AsyncSession, item: ModelType):
  await session.delete(item)
  await session.commit()
  return {'message': 'Item eliminado correctamente'}