from random import randint
from sys import exit
from copy import deepcopy
from rooms import *
from items import *
from characters import *

class Map(object):
	rooms = {
		"entrance": Room("entrance", "You stand near the large cave entrance. To your north lies the unknown.", 
						 adjacent = {"north": "hallway"}),
		"hallway":  Room("hallway", "You are in the great hall.", 
						 adjacent = {"south": "entrance", "east": "pit"}, 
						 items = [Weapon('mace', 'weapon', 5)],
						 monsters = [Character("Goblin", 5)]),
		"pit":		Room("pit", "You enter the great pit in the ground.",
						 adjacent = {"west": "hallway"},
						 items = [],
						 monsters = [Character("Imp", 3)]),
		"death": 	Death("death", "You feel numbness and cold. You die.")
	}

	def __init__(self, start_room):
		self.start_room = start_room
		
	def next_room(self, room):
		return self.rooms[room].enter()
		
	def start(self):
		return self.rooms[self.start_room].enter()
	
class Engine(object):

	def __init__(self, map):
		self.map = map
		
	def play(self):
		player = Player("You", 10, 10)
		room = self.map.start()
		while True:
			choices = raw_input("> ")
			choices = choices.split(' ')
			choice = choices[0]
			if choice == "attack" and self.map.rooms[room].monsters != []:
				fight = Fight(player, self.map.rooms[room].monsters[0])
				print fight.enter()
			elif choice == 'north' or choice == 'east' or choice == 'south' or choice == 'west':
				room = self.map.rooms[room].go(choice)
				room = self.map.next_room(room)
			elif choice == "show":
				if choices[1] == "inventory":
					player.show_inventory()
				if choices[1] == "equipment":
					player.show_equipped()
			elif choice == "equip":
				player.equip(choices[1])
			elif choice == "take" and self.map.rooms[room].items != []:
				idx = 0
				ok = 0
				for item in self.map.rooms[room].items:
					if item.name == choices[1]:
						player.take(self.map.rooms[room].items[idx])
						del self.map.rooms[room].items[idx]
						ok = 1
						break
					idx += 1
				if ok == 0:
					print "There is no %s here." % choices[1]
		
map = Map("entrance")
game = Engine(map)
game.play()