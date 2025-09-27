from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from database import get_session
from modelos import Customer, CustomerCreate, CustomerUpdate
from crud import *


router = APIRouter(prefix='/customers', tags=['customers'])


@router.post('/', response_model=Customer, status_code=status.HTTP_201_CREATED)
def create_customers(customer_data: CustomerCreate, session: Session = Depends(get_session)):
  db_customer = Customer.model_validate(customer_data)
  return create_item(session, db_customer)


@router.get('/', response_model=list[Customer])
def read_customer(session: Session = Depends(get_session)):
  return get_all_items(session, Customer)


@router.get('/{customer_id}', response_model=Customer)
def read_customer(customer_id: int, session: Session = Depends(get_session)):
  customer = get_item_by_id(session, Customer, customer_id)
  if not customer:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Customer no encontrado')
  return customer


@router.put('/{customer_id}', response_model=Customer)
def update_customer(customer_id, customer_data: CustomerUpdate, session: Session = Depends(get_session)):
  db_customer = get_item_by_id(session, Customer, customer_id)
  if not db_customer:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Customer no encontrado')
  update_customer = update_item(session, db_customer, customer_data.model_dump(exclude_unset=True))
  return update_customer


@router.delete('/{customer_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, session: Session = Depends(get_session)):
  db_customer = get_item_by_id(session, Customer, customer_id)
  if not db_customer:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'Customer no encotrado')
  delete_item(session, db_customer)
  return