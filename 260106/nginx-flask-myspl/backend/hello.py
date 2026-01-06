import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    """MySQL 데이터베이스 연결"""
    return mysql.connector.connect(
        host="redis",                    # TODO: DB 서비스 이름 (compose.yaml 참조)
        user="root",
        password=os.environ.get("???"), # TODO: 환경변수 이름
        database="example"
    )

def init_db():
    """테이블이 없으면 생성"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    """방문 기록 저장 및 조회"""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()

    # 방문 기록 추가
    cursor.execute("INSERT INTO visits () VALUES ()")
    conn.commit()

    # 총 방문 수 조회
    cursor.execute("SELECT COUNT(*) FROM visits")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return f"""
    <h1>🐳 Docker Compose 3-Tier 아키텍처</h1>
    <p>Nginx → Flask → MySQL 연결 성공!</p>
    <p>총 방문 횟수: <strong>{count}</strong></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)