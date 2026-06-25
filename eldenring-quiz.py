print("############## BEM VINDO AO QUIZ DE ELDEN RING ##############")
answer_start = input("Deseja começar? (S/N)").upper()

if answer_start != "S":
    print("Finalizando jogo!")
    quit()

name = input("Digite o seu nome: ")
print(f"\nCerto {name}, vamos começar!")
score = 0

print("\n1) Em que ano foi lançado Elden Ring?\n(A) 2020\n(B) 2021\n(C) 2022\n(D) 2023\n")
answer_1 = input("Resposta: ")

if answer_1.upper() == "C":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("2) Quem é o desenvolvedor de Elden Ring?\n(A) Ubisoft\n(B) FromSoftware\n(C) EA Games\n(D) Rockstar Games\n")
answer_2 = input("Resposta: ")

if answer_2.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("3) Qual é o nome do mundo de Elden Ring?\n(A) Tamriel\n(B) As Terras Intermédias\n(C) Hyrule\n(D) Midgard\n")
answer_3 = input("Resposta: ")

if answer_3.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("4) Quem ajudou na criação da história de Elden Ring?\n(A) J.K. Rowling\n(B) George R. R. Martin\n(C) Stephen King\n(D) J.R.R. Tolkien\n")
answer_4 = input("Resposta: ")

if answer_4.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("5) Qual é o objetivo principal do jogo?\n(A) Construir cidades\n(B) Tornar-se o Lorde Prístino (Elden Lord)\n(C) Sobreviver a zumbis\n(D) Ganhar corridas\n")
answer_5 = input("Resposta: ")

if answer_5.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("6) Em qual área Malenia é encontrada?\n(A) Montanhas dos Gigantes\n(B) Árvore Sacra\n(C) Leyndell, Capital Real\n(D) Caelid\n")
answer_6 = input("Resposta: ")

if answer_6.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("7) Qual status Malenia aplica com seus ataques?\n(A) Congelamento\n(B) Sangramento\n(C) Podridão Escarlate\n(D) Loucura\n")
answer_7 = input("Resposta: ")

if answer_7.upper() == "C":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("8) Qual item está ligado diretamente à história de Malenia e Miquella?\n(A) Ouro Puro\n(B) Runa Arcana\n(C) Lágrima Larval\n(D) Pedra de Forja Sombria\n")
answer_8 = input("Resposta: ")

if answer_8.upper() == "A":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("9) Qual é o nome da forma final de Malenia?\n(A) Deusa da Podridão\n(B) Lâmina de Miquella\n(C) Rainha Escarlate\n(D) Imperatriz da Rot\n")
answer_9 = input("Resposta: ")

if answer_9.upper() == "A":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("10) O que acontece quando Malenia acerta golpes no jogador?\n(A) Ela perde vida\n(B) Ela se cura parcialmente\n(C) Ela fica mais lenta\n(D) Ela fica invencível\n")
answer_10 = input("Resposta: ")

if answer_10.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("11) Qual foi o primeiro grande chefe obrigatório do jogo Elden Ring?\n(A) Radahn, Flagelo das Estrelas\n(B) Godrick, o Enxertado\n(C) Malenia, Lâmina de Miquella\n(D) Rennala, Rainha da Lua Cheia\n")
answer_11 = input("Resposta: ")

if answer_11.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("12) O que são as Grandes Runas em Elden Ring?\n(A) Armas lendárias\n(B) Fragmentos do poder dos semideuses\n(C) Feitiços proibidos\n(D) Itens de cura\n")
answer_12 = input("Resposta: ")

if answer_12.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("13) Qual personagem está diretamente ligado à missão da Ranni?\n(A) Blaidd\n(B) Hewg\n(C) Gostoc\n(D) Enia\n")
answer_13 = input("Resposta: ")

if answer_13.upper() == "A":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("14) Qual é o efeito principal da Podridão Escarlate?\n(A) Congelamento progressivo\n(B) Dano contínuo ao longo do tempo\n(C) Redução de velocidade apenas\n(D) Envenenamento leve\n")
answer_14 = input("Resposta: ")

if answer_14.upper() == "B":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("15) Qual é o nome do reino onde fica a Árvore Sacra?\n(A) Caelid\n(B) Liurnia\n(C) Elphael\n(D) Limgrave\n")
answer_15 = input("Resposta: ")

if answer_15.upper() == "C":
    print("Correto!\n")
    score = score + 1
else:
    print("Incorreto.\n")


print("##################################################\n")
print(f"Parabéns, {name}!! A sua pontuação é de: {score}/15")