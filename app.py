from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route("/")
def exibir_home():
    return render_template("home.html")

@app.route("/contato")
def exibir_contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)