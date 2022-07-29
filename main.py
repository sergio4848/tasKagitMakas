import random
choices = ["Taş", "Kağıt", "Makas"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Taş, Kağıt or  Makas?").capitalize()
    ## Conditions of Taş,Kağıt and Makas
    if player == computer:
        print("Berabere!")
    elif player == "Taş":
        if computer == "Kağıt":
            print("Kaybettin!", computer, "sarar", player)
            cpu_score+=1
        else:
            print("Kazandın!", player, "parçalar", computer)
            player_score+=1
    elif player == "Kağıt":
        if computer == "Makas":
            print("Kaybettin!", computer, "keser", player)
            cpu_score+=1
        else:
            print("Kazandın!", player, "sarar", computer)
            player_score+=1
    elif player == "Makas":
        if computer == "Taş":
            print("Kaybettin...", computer, "parçalar", player)
            cpu_score+=1
        else:
            print("Kazandın!", player, "keser", computer)
            player_score+=1
    elif player=='End':
        print("Sonuç:")
        print(f"CPU:{cpu_score}")
        print(f"Oyuncu:{player_score}")
        break