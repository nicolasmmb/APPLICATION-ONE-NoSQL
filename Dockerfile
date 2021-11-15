FROM python:3.8.8

WORKDIR /

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "alembic", "upgrade", "48fa24973d26" ]
#CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]

