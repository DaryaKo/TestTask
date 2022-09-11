from datetime import datetime
from typing import Optional
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'


class EmployeeSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    age: int = Field(..., gt=0, lt=150)
    company: str = Field(...)
    join_date: datetime = Field(default=datetime.now())
    job_title: str = Field(...)
    gender: Gender = Field(..., alias='Gender')
    salary: int = Field(..., gt=0)

    class Config:
        schema_extra = {
            "example": {
                "name": "Cedric Page",
                "email": "a.facilisis.non@cursus.com",
                "age": 63,
                "company": "Yandex",
                "join_date": "2001-06-10T19:08:52-07:00",
                "job_title": "janitor",
                "gender": "male",
                "salary": 9688
            }
        }


class Employee(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: Gender
    salary: int


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}