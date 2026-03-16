import random

#fazendo o inicio 
print("""       /$$  /$$            /$$           /$$                                                                                                      
                | $$|__/           |__/          | $$                                                                                                      
  /$$$$$$   /$$$$$$$ /$$ /$$    /$$ /$$ /$$$$$$$ | $$$$$$$   /$$$$$$         /$$$$$$        /$$$$$$$  /$$   /$$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
 |____  $$ /$$__  $$| $$|  $$  /$$/| $$| $$__  $$| $$__  $$ /$$__  $$       /$$__  $$      | $$__  $$| $$  | $$| $$_  $$_  $$ /$$__  $$ /$$__  $$ /$$__  $$
  /$$$$$$$| $$  | $$| $$ \  $$/$$/ | $$| $$  \ $$| $$  \ $$| $$$$$$$$      | $$  \ $$      | $$  \ $$| $$  | $$| $$ \ $$ \ $$| $$$$$$$$| $$  \__/| $$  \ $$
 /$$__  $$| $$  | $$| $$  \  $$$/  | $$| $$  | $$| $$  | $$| $$_____/      | $$  | $$      | $$  | $$| $$  | $$| $$ | $$ | $$| $$_____/| $$      | $$  | $$
|  $$$$$$$|  $$$$$$$| $$   \  $/   | $$| $$  | $$| $$  | $$|  $$$$$$$      |  $$$$$$/      | $$  | $$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$      |  $$$$$$/
 \_______/ \_______/|__/    \_/    |__/|__/  |__/|__/  |__/ \_______/       \______/       |__/  |__/ \______/ |__/ |__/ |__/ \_______/|__/       \______/ 
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                    
                                                                           __________
                                                                          | ________ |
                                                                          ||12345678||
                                                                          |..........|
                                                                          |[M|#|C][-]|
                                                                          |[7|8|9][+]|
                                                                          |[4|5|6][x]|
                                                                          |[1|2|3][%]|
                                                                          |[.|O|:][=]|
                                                                          "----------"

         
                                                """)

#escolhendo numero

nivel = int(input("""
         ********************************
         *    1-Noob (de 1 à 10)        *
         *    2-Médio (de 1 à 20)       *
         *   3-Profissional (de 1 à 50) *
         *    4-SENAI (de 1 à 200)      *
         ********************************
      
             ESCOLHA O NÍVEL: """))

if nivel == 1: 
    numero_aleatorio = random.randrange(1,10)
    chute = int(input("escolha um número de um à dez: "))
    if chute == numero_aleatorio:
        print("parabéns você acertou!")
    else:
        print(f"você errou! o número era: {numero_aleatorio}")

if nivel == 2: 
    numero_aleatorio = random.randrange(1,20)
    chute = int(input("escolha um número de um à vinte: "))
    if chute == numero_aleatorio:
        print("parabéns você acertou!")
    else:
        print(f"você errou! o número era: {numero_aleatorio}")

if nivel == 3: 
    numero_aleatorio = random.randrange(1,50)
    chute = int(input("escolha um número de um à cinquenta: "))
    if chute == numero_aleatorio:
        print("parabéns você acertou!")
    else:
        print(f"você errou! o número era: {numero_aleatorio}")

if nivel == 4: 
    numero_aleatorio = random.randrange(1,200)
    chute = int(input("escolha um número de um à duzentos: "))
    if chute == numero_aleatorio:
        print("parabéns você acertou!")
    else:
        print(f"você errou! o número era: {numero_aleatorio}")