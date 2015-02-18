from random import randint
from sys import exit
from copy import deepcopy

class Room(object):
	
	def __init__(self, name, desc, adjacent = {}, items = [], monsters = []):
		self.name = name
		self.desc = desc
		self.adjacent = adjacent
		self.items = items
		self.monsters = monsters
		
	def enter(self):
		print self.desc
		if self.monsters != []:
			for monster in self.monsters:
				print "There is %s here." % monster.name
		if self.items != []:
			for item in self.items:
				print "You see %s lying here." % item.name
		for k in self.adjacent.keys():
			print "To your %s is %s" % (k, self.adjacent[k])
		return self.name
		
	def go(self, direction):
		next_room = self.adjacent.get(direction, None)
		if next_room != None:
			next_room.enter()
		else:
			print "You can't go there."
		
class Death(Room):
	
	def __init__(self, name, desc):
		super(Death, self).__init__(self, name, desc)
	
	def enter(self):
		print self.desc
		exit(1)

class Item(object):
	
	def __init__(self):
		print "A generic item, not to be instantiated."
		exit(1)

class Weapon(Item):
	
	def __init__(self, name, slot, dmg):
		self.name = name
		self.slot = slot
		self.dmg = dmg

class Armor(Item):
	
	def __init__(self, name, slot, prot):
		self.name = name
		self.slot = slot
		self.prot = prot

class Character(object):
	
	equipped = {}
	
	empty_slots = {
		"head": Armor("Nothing", "head", 0),
		"weapon": Weapon("Fists", "weapon", 1),
		"body": Armor("Plain clothes", "body", 1),
		"legs": Armor("Nothing", "legs", 0)
	}
	
	def __init__(self, name, hp, equipped = {}):
		self.name = name
		self.hp = hp
		if equipped == {}:
			self.equipped = deepcopy(self.empty_slots)
		else:
			self.equipped = equipped

class Player(Character):
	inventory = [Armor("helmet", "head", 4), Weapon("knife", "weapon", 3)]
	
	def __init__(self, name, hp, inv_cap, equipped = {}, inventory = []):
		if inventory != []:
			self.inventory = inventory
		self.inv_cap = inv_cap
		super(Player, self).__init__(name, hp, equipped = {})
	
	def equip(self, item):
		idx = 0
		for piece in self.inventory:
			if piece.name == item:
				current = self.equipped[piece.slot]
				print "You equip", item
				self.equipped[piece.slot] = piece
				del self.inventory[idx]
				if current.name != self.empty_slots[current.slot].name:
					self.inventory.append(current)
				return
			idx += 1
		print "You don't have", item
	
	def unequip(self, slot):
		# check if player has anything in the slot (map with nothings maybe?)
		# remove existing item, change it with nothings
		# check if item fits in inventory, if it is - put it there, if not - drop
		pass
		
	def take(self, item):
		if len(self.inventory) < self.inv_cap:	
			print "You pick up", item.name
			self.inventory.append(item)
		else:
			print "You cannot carry anymore."
	
	def drop(self, item):
		idx = 0
		for piece in self.inventory:
			if piece.name == item:
				del self.inventory[idx]
				return 
			else:
				print "You do not have ", item
			idx += 1
			
	def show_equipped(self):
		print "You wear:"
		for slot in ['head', 'weapon', 'body', 'legs']:
			if slot == 'weapon':
				stat = "%s weapon damage" % self.equipped[slot].dmg
			else:
				stat = "%s %s protection" % (self.equipped[slot].prot, slot)
			print " %6s: %15s (%s)" % (slot, self.equipped[slot].name, stat)
			
	def show_inventory(self):
		print "You have:"
		for item in self.inventory:
			if item.slot == 'weapon':
				stat = "%s weapon damage" % item.dmg
			else:
				stat = "%s %s protection" % (item.prot, item.slot)
			print "%6s (%s)" % (item.name, stat)
	
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
				if self.map.rooms[room].adjacent.get(choice, None) != None:
					room = self.map.rooms[room].adjacent[choice]
					room = self.map.next_room(room)
				else:
					print "You can't go there."
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

class Fight(object):
	
	def __init__(self, player, enemy):
		self.player = player
		self.enemy = enemy
		
	def enter(self):
		print "You're fighting ", self.enemy.name
		while self.player.hp > 0 and self.enemy.hp > 0:
			print "Choose 1 attack and 1 block zone from the list below:"
			print "Attack: 1. head, 2. body, 3. legs"
			print "Block:  1. head, 2. body, 3. legs"
			actions = raw_input("[combat]> ")
			actions = actions.split(' ')
			enemy_actions = "%d %d" % (randint(1, 3), randint(1, 3))
			enemy_actions = enemy_actions.split(' ')
			if actions[0] == enemy_actions[1]:
				print "Enemy blocks your attack!"
			else:
				print "You hit enemy for %d hp" % self.player.equipped['weapon'].dmg
				self.enemy.hp -= self.player.equipped['weapon'].dmg
			
			if actions[1] == enemy_actions[0]:
				print "You block enemy attack!"
			else:
				print "Enemy hits you for %d hp" % self.enemy.equipped['weapon'].dmg
				self.player.hp -= self.enemy.equipped['weapon'].dmg
			
		if self.player.hp <= 0:
			return 'death'
		else:
			return 'victory'
		
map = Map("entrance")
game = Engine(map)
game.play()