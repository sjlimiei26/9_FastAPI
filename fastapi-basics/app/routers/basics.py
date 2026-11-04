from fastapi import APIRouter

from app.schemas import ItemCreate

router = APIRouter()   # Spring의 Controller 분리와 동일함!

@router.get("/type")
def test_type(x: int):
    """
        FastAPI 에서는 타입 힌트가 곧 검증 규칙임!
    """
    return {"x": x, "type": type(x).__name__}

# [GET] /items/{item_id}?q=xx&limit=20
# -함수명 read_items
@router.get("/items/{item_id}")
def read_items(item_id: int, q: str | None = None, limit: int = 10):
    """
        * 경로 매개변수 : URL -> {item_id}. 매개변수 추가 시 이름을 동일하게 작성.
        * 쿼리 매개변수 : 그 외의 매개변수 (?q=xx&limit=xx)
        -> 기본값을 지정하게 되면 선택, 없으면 필수
    """
    return {"item_id": item_id, "q": q, "limit": limit}

# [POST] /items
# - 함수명 : create_item
@router.post("/items", status_code=201)  # status_code=201 : 성공 시 응답 코드를 201(Created)로 지정
def create_item(item: ItemCreate):
    """
        요청 Body / Pydantic 검증
        - 매개변수 타입이 BaseModel 이면 FastAPI가 JSON Body로 인식
    """
    return item

# [POST] /users
# - 함수명 : create_user
# - request body : {"username": "xxx", "password": "xxx"}
# - response : {"username": "xxx", "password": "xxx"}