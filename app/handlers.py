import uuid
from datetime import date, datetime
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from app.models import Point, Evidence, Base, Category
from app.forms import PointCreateForm, EvidenceCreateForm, EvidenceGetForm, PointGetForm, PointGetAllForm
from .database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", tags=["Main page"], response_model=List[PointGetAllForm])
def get_all_points(database=Depends(get_db)):
    points = database.query(Point).all()
    if not points:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such item")
    return points

@router.get("/point/{id}", response_model=PointGetForm, tags=["Managing evidences"])
def get_point(id:int, database=Depends(get_db)):
    exist = database.query(Point).filter(Point.point_id == id).one_or_none()
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no such point")
    # exist.category = Category[exist.category].value
    # print(vars(exist))
    return exist

# @router.get("/evidence/{id}", response_model=EvidenceGetForm)
# def get_evidence(id:int, database=Depends(get_db)):
#     exist = database.query(Evidence).filter(Evidence.rec_id == id).one_or_none()
#     if not exist:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no such record")
#     # exist.category = Category[exist.category].value
#     # print(vars(exist))
#     return exist


################ P O S T ###########################################
@router.post("/point", status_code=201, tags=["Managing evidences"])
def create_point(point_form:PointCreateForm = Body(...), database=Depends(get_db)):
    new_point = Point(
        set_date = point_form.set_date,
        location = point_form.location,
        description = point_form.description,
    )
    exist = database.query(Point).filter(Point.location == point_form.location).one_or_none()
    if exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="point already exist")
    database.add(new_point)
    database.commit()
    database.refresh(new_point)
    return status.HTTP_201_CREATED

@router.post("/evidence", status_code=201, tags=["Managing evidences"])
def create_evidence(evidence_form:EvidenceCreateForm = Body(...), database=Depends(get_db)):
    new_point = Evidence(
        point_id = evidence_form.point_id,
        category = evidence_form.category.value ,
        file_link = evidence_form.file_link,
    )

    database.add(new_point)
    database.commit()
    database.refresh(new_point)
    return status.HTTP_201_CREATED

