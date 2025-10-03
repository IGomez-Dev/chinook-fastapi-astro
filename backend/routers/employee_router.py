from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_session
from modelos import Employee, EmployeeCreate, EmployeeUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/employees', tags=['employees'])

session_dep = Annotated[AsyncSession, Depends(get_session)]


@router.post('/', response_model=Employee, status_code = status.HTTP_201_CREATED)
async def create_employee(employee_data: EmployeeCreate, session: session_dep):
  db_employee = Employee(**employee_data.model_dump())
  return await create_item(session, db_employee)


@router.get('/', response_model=list[Employee])
async def read_employees(session: session_dep):
  return await get_all_items(session, Employee)


@router.get('/{employee_id}', response_model=Employee)
async def read_employee(employee_id: int, session: session_dep):
  employee = await get_item_by_id(session, Employee, employee_id)
  if not employee:
    raise HTTPException(
      status_code=404,
      detail='Employee no encontrado'
    )
  return employee


@router.put('/{employee_id}', response_model=Employee)
async def update_employee(employee_id: int, employee_data: EmployeeUpdate, session: session_dep):
  db_employee = await get_item_by_id(session, Employee, employee_id)
  if not db_employee:
    raise HTTPException(
      status_code=404,
      detail='Employee no encontrado'
    )
  updated_employee = await update_item(session, db_employee, employee_data.model_dump(exclude_unset=True))
  return updated_employee


@router.delete('/{employee_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee(employee_id: int, session: session_dep):
  db_employee = await get_item_by_id(session, Employee, employee_id)
  if not db_employee:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Employee no encontrado'
    )
  await delete_item(session, db_employee)
  return