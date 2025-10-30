from flask import Flask, request, render_template, jsonify
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        # Safer evaluation (only math expressions)
        allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
        result = eval(expression, {"__builtins__": None}, allowed)
        return jsonify({"result": result})
    except:
        return jsonify({"error": "Invalid expression"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
