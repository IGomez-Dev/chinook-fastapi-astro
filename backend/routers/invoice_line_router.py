from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import InvoiceLine, InvoiceLineCreate, InvoiceLineUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/invoice_lines', tags=['invoice lines'])


session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=InvoiceLine, status_code=201)
async def create_invoice_line(invoice_line_data: InvoiceLineCreate, session: session_dep):
  db_invoice_line = InvoiceLine(**invoice_line_data.model_dump())
  return await create_item(session, db_invoice_line)


@router.get('/', response_model=list[InvoiceLine])
async def read_invoice_lines(session: session_dep):
  return await get_all_items(session, InvoiceLine)


@router.get('/{invoice_line_id}', response_model=InvoiceLine)
async def read_invoice_line(invoice_line_id: int, session: session_dep):
  invoice_line = await get_item_by_id(session, InvoiceLine, invoice_line_id)
  if not invoice_line:
    raise HTTPException(
      status_code=404,
      detail='Invoice Line no encontrado'
    )
  return invoice_line


@router.put('/{invoice_line_id}', response_model=InvoiceLine)
async def update_invoice_line(invoice_line_id: int, invoice_line_data: InvoiceLineUpdate, session: session_dep):
  invoice_line = await get_item_by_id(session, InvoiceLine, invoice_line_id)
  if not invoice_line:
    raise HTTPException(
      status_code=404,
      detail='Invoice Line no encontrado'
    )
  invoice_line = await update_item(session, invoice_line, invoice_line_data.model_dump(exclude_unset=True))
  return invoice_line


@router.delete('/{invoice_line_id}', status_code=204)
async def delete_invoice_line(invoice_line_id: int, session: session_dep):
  invoice_line = await get_item_by_id(session, InvoiceLine, invoice_line_id)
  if not invoice_line:
    raise HTTPException(
      status_code=404,
      detail='Invoice Line no encontrado'
    )
  await delete_item(session, invoice_line)
  return