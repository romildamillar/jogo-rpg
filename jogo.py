def iniciar_jogo():
    return {
        "fase": "inicio",
        "mensagem": "Você é um guerreiro em uma terra cheia de perigos.",
        "vida_jogador": 100,
        "vida_monstro": 50,
        "nivel": 1
    }

def escolha_caminho(estado, escolha):
    if escolha == "1":
        estado["fase"] = "batalha"
        estado["mensagem"] = "Você decidiu ajudar a aldeia. Os aldeões estão gratos!"
    elif escolha == "2":
        estado["fase"] = "caverna"
        estado["mensagem"] = "Você entrou na caverna e encontrou um baú misterioso."
    elif escolha == "3":
        estado["fase"] = "castelo"
        estado["mensagem"] = "No castelo, o rei pede sua ajuda em uma missão importante."
    return estado

def batalha(estado, acao):
    if acao == "atacar":
        estado["vida_monstro"] -= 10
        estado["mensagem"] = f"Você atacou o monstro e causou 10 de dano!"
    elif acao == "defender":
        estado["mensagem"] = "Você se defendeu!"
    elif acao == "usar_item":
        estado["vida_jogador"] += 10
        estado["mensagem"] = "Você usou um item e recuperou 10 de vida!"

    # Ataque do monstro
    estado["vida_jogador"] -= 5

    # Checar vitória/derrota
    if estado["vida_jogador"] <= 0:
        estado["fase"] = "derrota"
        estado["mensagem"] = "Você foi derrotado!"
    elif estado["vida_monstro"] <= 0:
        estado["fase"] = "vitoria"
        estado["mensagem"] = "Você venceu a batalha!"

    return estado
