from datetime import datetime
from os import PRIO_USER
from typing import Optional

from fastapi import APIRouter, HTTPException, status, Query
from fastapi_pagination import Page, add_pagination, paginate
from pydantic import EmailStr
from pymongo.errors import ServerSelectionTimeoutError, NetworkTimeout

from server.crud.employees import (
    list_employees,
)
from server.models.employees import (
    Employee,
    Gender,
)


server_router = APIRouter()


@server_router.get("/",
    response_model=Page[Employee],
    response_description="Employees list")
async def get_employees(
    name: Optional[str] = None,
    email: Optional[EmailStr] = None,
    age__gt: Optional[int] = Query(default=None, gt=0, lt=150),
    age__lt: Optional[int] = Query(default=None, gt=0, lt=150),
    company: Optional[str] = None,
    join_date__gt: Optional[datetime] = None,
    join_date__lt: Optional[datetime] = None,
    job_title: Optional[str] = None,
    gender: Optional[Gender] = None,
    salary__gt: Optional[int] = Query(default=None, gt=0),
    salary__lt: Optional[int] = Query(default=None, gt=0),
):
    filters = {}
    gt_lt_filters = {"age": [age__gt, age__lt], "salary": [salary__gt, salary__lt], "join_date": [join_date__gt, join_date__lt]}
    simple_filters = {"gender": gender}
    icontains_filters = {"name": name, "email": email, "company": company, "job_title": job_title}
    for field_name, gt_lt in gt_lt_filters.items():
        if any(gt_lt):
            filters[field_name] = {**({'$gt': gt_lt[0]} if gt_lt[0] else {}), **({'$lt': gt_lt[1]} if gt_lt[1] else {})}
    for field_name, value in simple_filters.items():
        if value:
            filters[field_name] = value
    for field_name, value in icontains_filters.items():
        if value:
            filters[field_name] = {"$regex": f".*{value}.*$", "$options": "i"}
    try:
        employees = await list_employees(filters)
    except (ServerSelectionTimeoutError, NetworkTimeout):
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail='The server is currently unable to handle the incoming requests')
    return paginate(employees)

add_pagination(server_router)