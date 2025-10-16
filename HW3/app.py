from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/profile", methods=["POST"])
def profile():
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    bio = request.form.get("bio")

    return render_template("result.html",name=name, age=age, gender=gender, bio=bio)

if __name__ == "__main__":
    app.run(debug=True)

