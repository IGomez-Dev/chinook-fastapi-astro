from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from database import get_session
from modelos import Employee, EmployeeCreate, EmployeeUpdate
from crud import *
from typing import Annotated


router = APIRouter(prefix='/employees', tags=['employees'])

session_dep = Annotated[Session, Depends(get_session)]


@router.post('/', response_class=Employee, status_code = status.HTTP_201_CREATED)
def create_employee(employee_data: EmployeeCreate, session: session_dep):
  db_employee = Employee.model_validate(employee_data)
  return create_item(session, db_employee)


@router.get('/', response_class=list[Employee])
def read_employees(session: session_dep):
  return get_all_items(session, Employee)


@router.get('/{employee_id}', response_model=Employee)
def read_employee(employee_id: int, session: session_dep):
  employee = get_item_by_id(session, Employee, employee_id)
  if not employee:
    raise HTTPException(
      status_code=404,
      detail='Employee no encontrado'
    )
  return employee


@router.put('/{employee_id}', response_model=Employee)
def update_employee(employee_id: int, employee_data: EmployeeUpdate, session: session_dep):
  db_employee = get_item_by_id(session, Employee, employee_id)
  if not db_employee:
    raise HTTPException(
      status_code=404,
      detail='Employee no encontrado'
    )
  update_employee = update_item(session, db_employee, employee_data.model_dump(exclude_unset=True))
  return update_employee


@router.employee('/{employee_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int, session: session_dep):
  db_employee = get_item_by_id(session, Employee, employee_id)
  if not db_employee:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Employee no encontrado'
    )
  delete_item(session, db_employee)
  return