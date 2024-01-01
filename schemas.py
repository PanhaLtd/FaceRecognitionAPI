from typing import List, Optional, Generic, TypeVar
from datetime import date, datetime
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class StudentSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    enname: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[date] = None
    pob: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    imagepath: Optional[str] = None

    class Config:
        orm_mode = True

class AttendanceSchema(BaseModel):
    date: Optional[date] = None
    id: Optional[int] = None
    name: Optional[str] = None
    scantime: Optional[datetime] = None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    student: Optional[T] = Field(...)


class RequestStudent(BaseModel):
    student: StudentSchema = Field(...)

class RequestAttendance(BaseModel):
    attendance: AttendanceSchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

class ResponseNoData(GenericModel):
    code: str
    status: str
    message: str