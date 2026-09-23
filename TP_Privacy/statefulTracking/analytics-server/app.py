from flask import Flask, request

app = Flask(__name__)


@app.before_request
def log_request():
    print(f"[ANALYTICS SERVER] {request.method} {request.path}")
    print(f"    Referer: {request.headers.get('Referer')}")
    print(f"    Cookie header received: {request.headers.get('Cookie')}")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9100, debug=True)