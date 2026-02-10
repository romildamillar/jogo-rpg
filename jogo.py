def iniciar_jogo():
    return {
        "vida": 100,
        "mensagem": "Você acorda em uma masmorra escura. Um inimigo aparece!"
    }

def atacar(estado):
    estado["vida"] -= 10
    estado["mensagem"] = "Você atacou o inimigo e perdeu 10 de vida!"
    return estado
