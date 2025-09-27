from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Customer, CustomerCreate, CustomerUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/customers', tags=['customers'])

session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customers(customer_data: CustomerCreate, session: session_dep):
  db_customer = Customer.model_validate(customer_data)
  return await create_item(session, db_customer)


@router.get('/', response_model=list[Customer])
async def read_customer(session: session_dep):
  return await get_all_items(session, Customer)


@router.get('/{customer_id}', response_model=Customer)
async def read_customer(customer_id: int, session: session_dep):
  customer = await get_item_by_id(session, Customer, customer_id)
  if not customer:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Customer no encontrado')
  return customer


@router.put('/{customer_id}', response_model=Customer)
async def update_customer(customer_id, customer_data: CustomerUpdate, session: session_dep):
  db_customer = await get_item_by_id(session, Customer, customer_id)
  if not db_customer:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Customer no encontrado')
  update_customer = await update_item(session, db_customer, customer_data.model_dump(exclude_unset=True))
  return update_customer


@router.delete('/{customer_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: int, session: session_dep):
  db_customer = await get_item_by_id(session, Customer, customer_id)
  if not db_customer:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'Customer no encotrado')
  await delete_item(session, db_customer)
  return