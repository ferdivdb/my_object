'''
author : ferdivdb
date : 19/12/2021

'''
class Player:
	def __init__(self, pseudo, health, attack):
		self.pseudo = pseudo
		self.health = health
		self.attack = attack
		print("Bienvenue au joueur", pseudo, "/ Points de vie:", health, "/ Attack:", attack)

	def get_pseudo(self):
		return self.pseudo

	def get_health(self):
		return self.health

	def get_attack_value(self):
		return self.attack

	def damage(self, damage): # Methode recevoir des dégats
		self.health -= damage

	def attack_player(self, target_player): # Methode pour attaquer
		target_player.damage(self.attack)