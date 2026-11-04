"""
    Pydantic 모델 : 요청/응답 데이터의 모양과 검증 규칙을 정의
"""
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    """
        - name : 1 ~ 50자 문자열
        - price : 0보다 큰 정수 gt
    """
    name: str = Field(min_length=1, max_length=50)
    price: int = Field(gt=0)