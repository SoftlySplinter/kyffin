from flask import Flask
from flask import render_template

def run():
    app=Flask("Kyffin")
    
    @app.route("/")
    def hello():
        return render_template("home.html")

    app.run(debug=True)
