from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    #rpta = open(index.html,"w")
    rpta = "<h1> Hola Mundo </h1>"
    return rpta

if __name__ == "__main__":
	app.run()	
