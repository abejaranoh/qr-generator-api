from fastapi import FastAPI
from .routes.create_qr import qr
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(qr)

handler = Mangum(app=app)