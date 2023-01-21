from fastapi import FastAPI
from .routes.create_qr import qr

app = FastAPI()

app.include_router(qr)