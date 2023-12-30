FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install fastapi==0.68.0 uvicorn==0.15.0 tensorflow==2.8.0 numpy==1.21.2 sqlalchemy==1.4.25 typing_extensions==3.10.0.0 \
                       psycopg2==2.9.1 opencv-python==4.5.3.56 Pillow==8.3.1

RUN pip install protobuf==3.20.0

RUN pip install --upgrade typing-extensions

RUN pip install aiofiles

COPY . /app/app

WORKDIR /app/app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]