from flask import Flask

def run():
    app=Flask("Kyffin")
    
    @app.route("/")
    def hello():
        return "Hello World"

    app.run()
