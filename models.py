from sqlalchemy import  Column, Integer, String
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