from flask import Flask,render_template, request
from password_checker import overall_strength

app= Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    result=None
    if request.method=="POST":
        pw=request.form["password"]
        result=overall_strength(pw)
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(debug=True)