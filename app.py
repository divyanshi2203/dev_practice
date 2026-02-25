from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def home():
    return "You feel like my home Sagar ki divu."

@app.route("/make_babies")
def evara():
    return jsonify(Mommy = "Divu",
            Daddy = "sagar"),201
@app.route("/child")
def baby():
    name = request.args.get("name")
    diff = int(request.args.get("diff"))
    if diff>3:
        return jsonify(message= f"our daughter name will be {name}")
    elif diff <= 3 and diff > 5:
        return jsonify(message = f"our son will be named as {name}")
    else:
        return "Sorry, we are not planning for a baby anymore.!!!"
@app.route("/couple/<string:husband>/<string:wife>")
def couple(husband:str,wife:str):
    return jsonify(message=f"{husband} is a husband of {wife}")
print("Hey baby")
print("hey")
print("No pull request")
print("again")

if __name__ == "__main__":
    app.run(debug=True)
