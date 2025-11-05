from flask import Flask

# __name__ = "main" -> executado de forma manual, e não importado por outro arquivo
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Página sobre"

# Garantir que só vai subir o servidor dessa forma se for executado de forma manual -> desenvolvimento local
if __name__ == "__main__":
    app.run(debug=True)