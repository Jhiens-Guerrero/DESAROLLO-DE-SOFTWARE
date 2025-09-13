from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": os.getenv("MESSAGE", "Hello"),
        "release": os.getenv("RELEASE", "v0")
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"Starting app on port {port}...")
    app.run(host="0.0.0.0", port=port)
