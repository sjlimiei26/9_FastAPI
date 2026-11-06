"""
    DB 연결 설정

    [사전 준비]
    - sqlalchemy 설치
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

DATABASE_URL = 'sqlite:///./todo.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    """ ORM 모델의 부모 클래스 """

def get_db():
    """
        DB 세션을 요청마다 생성하고 주입 (응답 후 닫음)
    """
    db: Session = SessionLocal()

    try:
        yield db        # 생성한 Session 반환 후 멈춤
    finally:
        db.close()