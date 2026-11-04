from fastapi import FastAPI

from app.routers import basics

app = FastAPI()

# 라우터 등록
app.include_router(basics.router)


@app.get("/")
def test_root():
    return {"message": "Hello, FastAPI!"}