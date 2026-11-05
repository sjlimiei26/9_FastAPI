"""
    공통으로 사용하는 의존성 모음
"""
from fastapi import Query

def pagination(
        skip: int = Query(0, ge=0, description="건너뛸 개수"),
        limit: int = Query(10, ge=1, le=100, description="가져올 개수")
) -> dict:
    """
        - skip : 0 이상 (default: 0)
        - limit : 1 이상 100 이하 (default: 10)
        * ge : 최솟값
        * le : 최댓값
    """
    return {"skip": skip, "limit": limit}