# Python 3.9 slim 이미지
FROM python:3.9-slim

# 작업 디렉토리
WORKDIR /app

# 의존성 먼저 설치 (캐시 활용)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사 (개발 시에는 볼륨 마운트로 대체)
COPY . .

# Streamlit 포트
EXPOSE 8501

# Streamlit 실행 (Hot Reload 활성화)
# --server.runOnSave=true: 파일 저장 시 자동 새로고침
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.runOnSave=true"]
