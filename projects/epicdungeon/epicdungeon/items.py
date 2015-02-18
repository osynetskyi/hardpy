from sys import exit

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