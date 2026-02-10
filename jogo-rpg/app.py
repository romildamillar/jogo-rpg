from flask import Flask, render_template, request, session
from jogo import iniciar_jogo, atacar

app = Flask(__name__)
app.secret_key = "rpg-secreto"

@app.route("/", methods=["GET", "POST"])
def index():
    if "estado" not in session:
        session["estado"] = iniciar_jogo()

    if request.method == "POST":
        acao = request.form.get("acao")
        if acao == "atacar":
            session["estado"] = atacar(session["estado"])

    return render_template("index.html", estado=session["estado"])

if __name__ == "__main__":
    app.run()
