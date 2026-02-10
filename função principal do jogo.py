Função Principal do Jogo
#jogo RPG
#Criado por: Romilda Millar
#Data:2025-04-14
#Versão: 1.0.0
#Descrição: Jogo RPG de Aventura
#Importando bibliotecas necessárias

# Função principal do jogo
def jogo_rpg():
    print("Nome Do jogo RPG")
    print("Nome do jogo é Floresta sombria\n")
    print("Bem-vindo ao RPG!\n")
    

# Introdução da história

def introducao():
    print("Você é um guerreiro em uma terra cheia de perigos e mistérios.")
    print("Sua jornada começa em uma aldeia serena cercada por montanhas imponentes")
    print("A brisa fresca carrega o som de pássaros, enqunto fumaça sobe das chaminés das casas.")
    print("Você sente a emoção de uma nova aventura á sua frente.")
    print("Você pode escolher seu próprio caminho diferente.")
    
# Escolhas iniciais função

def escolha_caminho():
    print("\nEscolha seu caminho:")
    print("1. Ajudar uma aldeia atacada por monstros.")
    print("2. Explorar uma caverna escura.")
    print("3. Visitar o castelo em busca de trabalho.")
    
    try:
        escolha = int(input("\nO que você deseja fazer? (Digite 1, 2 ou 3): "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return escolha_caminho()  # Repete a função se entrada for inválida
        
    if escolha == "1":
        print("\nVocê decide ajudar a aldeia. Os aldeões estão assustados e gratos por sua ajuda!")
        batalha(1)
    elif escolha == "2":
        print("\nVocê entra na caverna e encontra um baú misterioso com um artefato mágico.")
    elif escolha == "3":
        print("\nNo castelo, o rei pede sua ajuda em uma missão importante!")
    else:
        print("\nEscolha inválida. Por favor, tente novamente.")
        escolha_caminho(2)


# Função de batalha
def batalha(nivel):
    print(f"\nVocê entra em uma batalha de nível {nivel}!")
    print("Prepare-se para lutar contra os monstros!")
    print("Você tem 100 pontos de vida.")
    print("Os monstros têm 50 pontos de vida.") 
    Vida_jogador = 100
    Vida_monstro = 50
    
    while Vida_jogador > 0 and Vida_monstro > 0:
        print("\nEscolha sua ação:")
        print("1. Atacar")
        print("2. Defender")
        print("3. Usar item")
        print("4. Fugir")
        try:
            acao = int(input("Digite o número da ação: "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue
        
        if acao == 1: #Atacar
            dano = 10  # valor fixo para ataque
            
            Vida_monstro -= dano
    
            print(f"\nVocê atacou o monstro e causou {dano} de dano!")
        elif acao == 2: #Defender
            print("\nVocê se defendeu! reduziu o dano do proxímo ataque co mostro.")
        elif acao == 3: #Usar item
            Vida_jogador += 10 #Exemplo de recuperação de vida
            print("\nVocê usou um item e recuperou 10 pontos de vida!")
        else:
            print("Ação invalida. Tente novamente.")
            continue
        
        # Ataque do monstro
        dano_monstro = 5 #valor fixo para ataque do mostro
        
        Vida_jogador -= dano_monstro
        print(f"\nO monstro atacou você e causou {dano_monstro} de dano!")
        
        #Exibir o status atual
        
        print(f"\nSua vida: {Vida_jogador}")
        print(f"Vida do monstro: {Vida_monstro}")
        
        #Verifica quem venceu
        
        if Vida_jogador > 0:
            print("\nParabéns! Você venceu a batalha!")
            
        else:
            print("\nQue pena! Você foi derrotado!")
            
          
