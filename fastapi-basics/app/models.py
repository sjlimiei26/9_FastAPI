"""
    DB 테이블과 1:1로 대응되는 ORM 모델 모음

    'DB용' 모델만 정의.
    요청/응답 전용 모델은 schemas.py 에서 정의.
"""
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Todo(Base):
    """
        todos 테이블
    """
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)  # PK
    title: Mapped[str]      # NOT NULL
    done: Mapped[bool] = mapped_column(default=False)  # 기본값 지정