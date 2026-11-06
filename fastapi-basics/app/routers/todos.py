from fastapi import APIRouter

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