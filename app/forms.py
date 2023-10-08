from datetime import date

from pydantic import BaseModel
from typing import List, Optional
from .models import Category

class PointCreateForm(BaseModel):
    set_date: date
    location: str
    description: str

    class Config:
        orm_mode = True


class EvidenceCreateForm(BaseModel):
    point_id: int
    category: Category
    file_link: str

    class Config:
        orm_mode = True


class EvidenceGetForm(BaseModel):
    rec_id: int
    point_id: int
    category: Category
    file_link: str

    class Config:
        orm_mode = True

class PointGetForm(BaseModel):
    point_id: int
    set_date: date
    location: str
    evidens: List[EvidenceGetForm] = []

    class Config:
        orm_mode = True

class PointGetAllForm(BaseModel):
    point_id: int
    set_date: date
    location: str

    class Config:
        orm_mode = True