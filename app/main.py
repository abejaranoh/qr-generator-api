from fastapi import FastAPI
from routes.user import user

app = FastAPI()

# app.include_router(qr)
app.include_router(user)

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}