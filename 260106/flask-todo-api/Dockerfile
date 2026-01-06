# Python 3.11 slim 이미지 사용
FROM python:3.11-slim

# 작업 디렉토리
WORKDIR /app

# 의존성 먼저 설치(캐시 활용)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# --no-cache-dir : pip 캐시 저장 안함 -> 이미지 크기 감소

# 소스 코드 복사
COPY . .

# 포트
EXPOSE 5000

# 앱 실행
CMD ["python", "app.py"]