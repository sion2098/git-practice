from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 도메인에서 API 호출 허용

@app.route('/')
def home():
    return "Flask TODO API is running!"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# host='0.0.0.0' : 컨테이너 외부에서 접근 가능하게 함
# debug = True : 코드 변경 시 자동 재시작(Hot Reload)