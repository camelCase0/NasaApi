from datetime import date
from enum import Enum

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float, Table
from sqlalchemy.orm import Session, relationship

from app.config import DATABASE_URL

from .database import Base

class Category(Enum):
    Atmosphere = "Atmosphere"
    Biosphere = "Biosphere"
    LandSurface = "LandSurface"
    TerrestrialHydrosphere = "TerrestrialHydrosphere"
    Destruction = "Destruction"


class Point(Base):
    __tablename__ = 'point'
    
    point_id = Column(Integer, primary_key=True, index=True)
    set_date = Column(DateTime, default=date)
    location = Column(String)
    description = Column(String)

    evidens = relationship("Evidence", back_populates="point")
    
class Evidence(Base):
    __tablename__ = 'evidence'

    rec_id = Column(Integer, primary_key=True, index=True)
    
    point_id = Column(Integer, ForeignKey('point.point_id'))
    point = relationship("Point", back_populates="evidens")

    category = Column(String, default=Category.Destruction)
    file_link = Column(String)