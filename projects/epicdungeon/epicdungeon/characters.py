from random import randint
from copy import deepcopy
from items import *

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