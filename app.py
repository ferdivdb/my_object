'''
author : ferdivdb
date : 19/12/2021

'''
from os import system
from model.player import Player

system('clear')

player1 = Player("Ferdivdb", 20, 3)
player2 = Player("Bob", 20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())

print("Bienvenue au joueur", player1.get_pseudo(), "/ Points de vie:", player1.get_health(), "/ Attaque:", player1.get_attack_value())
print("Bienvenue au joueur", player2.get_pseudo(), "/ Points de vie:", player2.get_health(), "/ Attaque:", player2.get_attack_value())