# fastapi-basics
> Fastapi 기본 문법 연습 프로젝트

## 가상환경 준비
```bash
python -m venv .venv   # 가상환경 생성

.venv\Scripts\activate # 가상환경 활성화
.venv\Scripts\deactivate # 가상환경 비활성화
```

## 패키지/모듈 설치
```bash
pip install 모듈명
```

**현재 설치된 항목 파일 저장**
```bash
pip freeze > requirements.txt
```
**`requirements.txt` 파일 기준으로 모듈 설치**
```bash
pip install -r requirements.txt
```

## FastAPI 서버 실행
```bash
fastapi dev app/main.py
```
> **위의 가상환경 및 패키지 설치가 모두 완료된 상태여야 함**

---

## 디렉터리 구조
```
app/            # 소스폴더
    main.py     # 앱 생성, 라우터 등록, CORS 설정,...
    schemas.py  # Pydantic 모델 (DTO)
    routers/    # 라우팅 정보
        ...
        ...
```