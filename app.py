from flask import Flask

app = Flask(__name__)

@app.route("/")  # 브라우저에서 "/" 경로로 요청이 오면 아래 함수 실행
def hello_world():
    return "Hello, DevOps!"  # 브라우저에 표시할 문자열 반환

if __name__ == "__main__":  # 파이썬 파일을 직접 실행할 때만 서버 실행
    app.run(host="0.0.0.0", port=8080, debug=True)