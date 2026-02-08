from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "You feel like my home Sagar ki divu."

@app.route("/make_babies")
def evara():
    return jsonify(Mommy = "Divu",
            Daddy = "sagar"),201

if __name__ == "__main__":
    app.run(debug=True)