from flask import Flask, render_template, make_response, request
import secrets
app = Flask(__name__)

@app.route("/tracker")
def tracker():
    publisher = request.args.get("publisher", "unknown")
    page = request.args.get("page", "unknown")
    
    tid = request.cookies.get("tid")
    is_new = tid is None
    if is_new:
        tid = secrets.token_hex(8)
    
    
    resp = make_response(render_template("tracker.html",tid=tid,publisher=publisher))
    
    if is_new:
        resp.set_cookie(key="tid",value=tid)
    
    return resp


if __name__ == "__main__":
    app.run(host="tracker-one.local", port=8003, debug=True)
    
