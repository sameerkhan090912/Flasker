from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def hello():
    return "<h1> Hello world </h1>"

@app.errorhandler(404)
def pageNotFoundError(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def InternalServerErro(e):
    return render_template("500.html"),500

if __name__=="__main__":
    app.run(debug=True)
