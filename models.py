from sqlalchemy import  Column, Integer, String, PrimaryKeyConstraint
from config import Base

class Student(Base):
    __tablename__ ="student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    enname = Column(String)
    gender = Column(String)
    dob = Column(String)
    pob = Column(String)
    address = Column(String)
    phone = Column(String)
    imagepath = Column(String)

class Attendance(Base):
    __tablename__ ="attendance"

    date = Column(String)
    id = Column(Integer)
    name = Column(String)
    scantime = Column(String)

    __table_args__ = (
        PrimaryKeyConstraint('date', 'id'),
    )