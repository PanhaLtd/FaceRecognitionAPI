from fastapi import APIRouter, HTTPException, Path, UploadFile, File
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, StudentSchema, RequestStudent, ResponseNoData
import numpy as np
from PIL import Image
from io import BytesIO
import pipeline
import tensorflow as tf
import cv2
import os
from trainmodel import trainModel
from predictface import predictStudent


import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_face(img):
    haar = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")
    faces = haar.detectMultiScale(img,1.1,3)
    print(faces)
    for x,y,w,h in faces:
        pre_img = img[y:y+h,x:x+w] # crop image
        return pre_img

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@router.post("/addNewStudent")
async def add_new_student(request: RequestStudent, db: Session = Depends(get_db)):
    student = crud.add_student(db, student=request.parameter)
    return Response(status="Ok",
                    code="201",
                    message="Student is added successfully",
                    result = student
                    ).dict(exclude_none=True)

@router.get("/train")
async def train_model():
    message = trainModel()
    return ResponseNoData(status="Ok", code="200", message="hello")

@router.post("/addStudentVideo")
async def add_student_video(student_id: int, student_name: str, video: UploadFile):
    folder_name = f"Facedatabase/{student_id}_{student_name}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    video_path = f"{folder_name}/test.mp4"

    with open(video_path, "wb") as file:
        file.write(await video.read())
    face_cascade = cv2.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    img_id = 0
    while success and count < 100:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 3)
        print(count)
        print(faces)
        if(len(faces) != 0):
            for (x, y, w, h) in faces:
                # if (w > 100):
                    face_img = gray[y:y+h, x:x+w]
                    crop_face = cv2.resize(face_img, (224,224),cv2.INTER_AREA)
                    cv2.imwrite(f"{folder_name}/{img_id}.jpg", crop_face)
                    img_id += 1
                    success, image = vidcap.read()
        count += 1
    return ResponseNoData(status="Ok", code="200", message="Add new student successfully")

@router.get("/all")
async def get_all_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _students = crud.get_student(db)
    students = [StudentSchema(**student.__dict__) for student in _students]
    return Response(status="Ok", code="200", message="Success fetch all data", result=students)

@router.get("/{student_id}")
async def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db, student_id)
    if student:
        student_schema = StudentSchema(**student.__dict__)
        return Response[StudentSchema](status="Ok", code="200", message="Success fetch data", result=student_schema)
    else:
        return Response[None](status="Error", code="404", message="Student not found", result = None)

@router.post("/predict")
async def predict_student(
    file: UploadFile = File(...),  db: Session = Depends(get_db)
):
    image = read_file_as_image(await file.read())
    mybatch = cv2.resize(get_face(image),(224,224),cv2.INTER_AREA)

    class_name = predictStudent(mybatch)

    result = class_name.split("_")
    student_id = int(result[0])
    
    student = crud.get_student_by_id(db, student_id)
    if student:
        student_schema = StudentSchema(**student.__dict__)
        return Response[StudentSchema](status="Ok", code="200", message="Success fetch data", result=student_schema)
    else:
        return Response[None](status="Error", code="404", message="Student not found", result = None)

# @router.patch("/update")
# async def update_book(request: RequestBook, db: Session = Depends(get_db)):
#     _book = crud.update_book(db, book_id=request.parameter.id,
#                              title=request.parameter.title, description=request.parameter.description)
#     return Response(status="Ok", code="200", message="Success update data", result=_book)


# @router.delete("/delete")
# async def delete_book(request: RequestBook,  db: Session = Depends(get_db)):
#     crud.remove_book(db, book_id=request.parameter.id)
#     return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)