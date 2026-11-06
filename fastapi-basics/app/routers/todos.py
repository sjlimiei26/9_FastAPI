from fastapi import APIRouter, Depends

from app.schemas import TodoCreate, TodoOut
from app.database import get_db, Session
from app.models import Todo

"""
    TODO: 아래 REST API 명세에 맞게 매핑을 정의해봅시다.

    [GET]    /todos        할 일 목록 조회 (Read)
    [GET]    /todos/{id}   할 일 상세 조회 (Read)
    [POST]   /todos        할 일 등록(생성)(Create)
    [PATCH]  /todos/{id}   할 일 부분 수정 (Update)
    [DELETE] /todos/{id}   할 일 삭제 (Delete)
"""

# 공통 주소: /todos --> 라우팅 설정(등록)
router = APIRouter(prefix="/todos") 
# * prefix ---> Spring @RequestMapping

# [GET] /todos/health 
#  - response : "ok"
#  - 함수명 : health_check
@router.get("/health")
def health_check():
    return "ok"

# [GET]    /todos
@router.get("", response_model=list[TodoOut]) # -> /todos
def list_todos(db: Session = Depends(get_db)):

    query = db.query(Todo)

    return query.all()

# [GET]    /todos/{id}
@router.get("/{id}")
def read_todo(id: int):
    return id

# [POST]   /todos
# - request body : {title: "xxxxx"}
@router.post("")
def create_todo(body: TodoCreate,
                db: Session = Depends(get_db)):

    todo = Todo(title=body.title)

    db.add(todo)            # 저장할 객체 등록 (DB 처리 전)
    db.commit()             # DB에 적용

    db.refresh(todo)        # DB에 적용된 객체를 다시 읽어옴
    
    return todo

# [PATCH]  /todos/{id} 
@router.patch("/{id}")
def update_todo(id: int):
    return id


# [DELETE] /todos/{id}
@router.delete("/{id}")
def delete_todo(id: int):
    return id