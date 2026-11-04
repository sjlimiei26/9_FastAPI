from fastapi import APIRouter

router = APIRouter()   # Spring의 Controller 분리와 동일함!

@router.get("/type")
def test_type(x: int):
    """
        FastAPI 에서는 타입 힌트가 곧 검증 규칙임!
    """
    return {"x": x, "type": type(x).__name__}