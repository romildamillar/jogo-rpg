from flask import Flask, render_template, request, session
from jogo import iniciar_jogo, escolha_caminho, batalha

app = Flask(__name__)
app.secret_key = "rpg-secreto"

@app.route("/", methods=["GET", "POST"])
def index():
    if "estado" not in session:
        session["estado"] = iniciar_jogo()

    estado = session["estado"]

    if request.method == "POST":
        if estado["fase"] == "inicio":
            escolha = request.form.get("acao")
            estado = escolha_caminho(estado, escolha)
        elif estado["fase"] == "batalha":
            acao = request.form.get("acao")
            estado = batalha(estado, acao)

    session["estado"] = estado
    return render_template("index.html", estado=estado)

if __name__ == "__main__":
    app.run()
