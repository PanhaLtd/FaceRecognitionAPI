from sqlalchemy import  Column, Integer, String
from config import Base

class Student(Base):
    __tablename__ ="student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    dob = Column(String)
    image_path = Column(String)