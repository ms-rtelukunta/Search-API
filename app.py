from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    return jsonify({"query": query, "results": []})


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
