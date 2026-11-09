from fastapi import APIRouter, Depends, HTTPException

from app.schemas import TodoCreate, TodoOut, TodoUpdate
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
@router.get("/{id}", response_model=TodoOut)
def read_todo(id: int,
              db: Session = Depends(get_db)):

    """
    query = db.query(Todo)
    return query.filter(Todo.id == id).one()
    """
    todo = db.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")

    return todo

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
@router.patch("/{id}", response_model=TodoOut)
def update_todo(id: int, body: TodoUpdate,
                db: Session = Depends(get_db)):
    todo = db.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")

    # body.model_dump(exclude_unset=True) : 요청 시 전달된 데이터만 dict
    for key, value in body.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    
    return todo


# [DELETE] /todos/{id}
@router.delete("/{id}", status_code=204)  # 204 : 성공 후 응답 body가 없을 때 (=> return 필요 없음)
def delete_todo(id: int,
                db: Session = Depends(get_db)):

    todo = db.get(Todo, id)

    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")

    db.delete(todo)
    db.commit()

    # return id