import time
import redis
from flask import Flask

app = Flask(__name__)
# 'redis'는 compose.yaml에서 정의한 서비스 이름 = 호스트명
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    """Redis에서 방문 횟수 조회 (연결 실패 시 재시도)"""
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello Docker! I have been seen {count} times.\n'
