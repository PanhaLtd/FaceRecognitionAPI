from sqlalchemy.orm import Session
from models import Student, Attendance
from schemas import StudentSchema
from datetime import datetime


def get_student(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_student_attendance_by_id(db: Session, student_id: int):
    today_date = datetime.now().date()
    return db.query(Attendance).filter(Attendance.id == student_id).filter(Attendance.date == today_date).first()

def add_attendance(db: Session, student: StudentSchema):
    today_date = datetime.now().date()
    scan_time = datetime.now()
    _attendance = Attendance(
        date = today_date,
        id = student.id,
        name = student.name,
        scantime = scan_time
    )
    db.add(_attendance)
    db.commit()
    db.refresh(_attendance)
    return _attendance

def get_all_attendance(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Attendance).all()

def add_student(db: Session, student: StudentSchema):
    _student = Student(
        id = student.id,
        name = student.name,
        enname = student.enname,
        gender = student.gender,
        dob = student.dob,
        pob = student.pob,
        address = student.address,
        phone = student.phone,
        imagepath = student.imagepath
    )
    db.add(_student)
    db.commit()
    db.refresh(_student)
    return _student



# def create_book(db: Session, book: BookSchema):
#     _book = Book(title=book.title, description=book.description)
#     db.add(_book)
#     db.commit()
#     db.refresh(_book)
#     return _book


# def remove_book(db: Session, book_id: int):
#     _book = get_book_by_id(db=db, book_id=book_id)
#     db.delete(_book)
#     db.commit()


# def update_book(db: Session, book_id: int, title: str, description: str):
#     _book = get_book_by_id(db=db, book_id=book_id)

#     _book.title = title
#     _book.description = description

#     db.commit()
#     db.refresh(_book)
#     return _book