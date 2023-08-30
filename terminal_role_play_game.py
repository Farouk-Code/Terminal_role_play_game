import random

#Définition des variables globales
player_health = enemy_health = max_health = 50
potion = 3
player_attack = enemy_attack = None
care = None

#Afficher les règles du jeu
print("Vous devez battre votre ennemie, voici les règles du jeux :\n"
      "- Le jeu comporte deux joueurs : vous et un ennemi.\n"
      "- Vous commencez tous les deux avec 50 points de vie ❤️.\n"
      "- Votre personnage dispose de 3 potions 🧪 qui vous permettent de récupérer des points de vie.\n"
      "- L'ennemi ne dispose d'aucune potion.\n"
      "- Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.\n"
      "- Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.\n"
      "- L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.\n"
      "- Lorsque vous utilisez une potion, vous passez le prochain tour.")

#Début de la boucle
while player_health > 0 and enemy_health > 0:
    print("-" * 105)
    player_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

    #Vérifier que le joueur rentre le bon choix
    if player_choice != "1" and player_choice != "2":
        print("Veuillez rentrez un choix valide.")
    else:
        #Attaque
        if player_choice == "1":
            player_attack = random.randint(5, 10)
            enemy_health = enemy_health - player_attack
            enemy_attack = random.randint(5, 15)
            player_health = player_health - enemy_attack
            print(f"Vous avez infliger {player_attack} points de dégats à l'énnemie ⚔️")
            print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")

            #On vérifie si les deux joueurs ont plus de 0 de santé
            if player_health > 0 and enemy_health > 0:
                print(f"Il vous reste {player_health} points de vie")
                print(f"Il reste {enemy_health} points de vie à l'ennemie")
        #Soin        
        else:
            if potion > 0:
                care = random.randint(15, 50)
                player_health = player_health + care
                potion -= 1

                #Vérifier on a atteint le maximum en santé
                if player_health >= max_health:
                    player_health = max_health
                    print(f"Votre santé est au maximum ({potion} 🧪 restantes)")
                else:
                    print(f"Vous récupérez {care} points de vie ❤️  ({potion} 🧪 restantes)")
    
                enemy_attack = random.randint(5, 15)
                player_health = player_health - enemy_attack
                print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")
                
                #On vérifie si le joueur a toujour plus de 0 en santé
                if player_health > 0:
                    print(f"Il vous reste {player_health} points de vie")
                    print(f"Il reste {enemy_health} points de vie à l'ennemie")
                    print("-" * 105)
                    print("Vous avez passer votre tour...")
                    enemy_attack = random.randint(5, 15)
                    player_health = player_health - enemy_attack
                    print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")
                    print(f"Il vous reste {player_health} points de vie")
                    print(f"Il reste {enemy_health} points de vie à l'ennemie")
            else:
                print("Vous n'avez plus de potion...")
else:
    if enemy_health <= 0 and player_health <= 0:
        print("Vous avez tous les deux perdu... 💀💀")
    elif enemy_health <= 0:
        print("Bravo ! Vous avez gagné votre combat ! 💪")
    else:
        print("Vous avez perdu ce combat... 💀")