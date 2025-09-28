from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Invoice, InvoiceCreate, InvoiceUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/invoices', tags=['invoice'])


session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=Invoice, status_code=status.HTTP_201_CREATED)
async def create_invoice(invoice_data: InvoiceCreate, session: session_dep):
  invoice = Invoice(**invoice_data.model_dump)
  return await create_item(session, invoice)


@router.get('/', response_model = list[Invoice])
async def read_invoices(session: session_dep):
  return await get_all_items(session, Invoice)


@router.get('/{invoice_id}', response_model=Invoice)
async def read_invoice(invoice_id: int, session: session_dep):
  invoice = await get_item_by_id(session, Invoice, invoice_id)
  if not invoice:
    raise HTTPException (
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Invoice no encontrado'
    )
  return invoice


@router.put('/{invoice_id}', response_model=Invoice)
async def update_invoice(invoice_id: int, invoice_data: InvoiceUpdate, session: session_dep):
  invoice = await get_item_by_id(session, Invoice, invoice_id)
  if not invoice:
    raise HTTPException (
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Invoice no encontrado'
    )
  ud_invoice = await update_item(session, invoice, invoice_data.model_dump(exclude_unset=True)) 
  return ud_invoice


@router.delete('/{invoice_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_invoice(invoice_id: int, session: session_dep):
  invoice = await get_item_by_id(session, Invoice, invoice_id)
  if not invoice:
    raise HTTPException (
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Invoice no encontrado'
    )
  await delete_item(session, invoice_id)
  return