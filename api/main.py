from fastapi import FastAPI
from .routes.create_qr import qr
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from decouple import config

# app = FastAPI()

# isProduction = config("IS_PRODUCTION")
# origins = ["*"]
origins = ["*://localhost:*/*"]

# if isProduction == True:
    # app = FastAPI(docs_url=None, redoc_url=None)
# else:
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(qr)

handler = Mangum(app=app)