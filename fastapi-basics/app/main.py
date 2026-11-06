from fastapi import FastAPI

from app.routers import basics, todos
from app.database import Base, engine

# 테이블 자동 생성 ---> 이미 존재하는 경우 건너뜀(패스)
Base.metadata.create_all(engine)

app = FastAPI()

# 라우터 등록
app.include_router(basics.router)
app.include_router(todos.router)

@app.get("/")
def test_root():
    return {"message": "Hello, FastAPI!"}