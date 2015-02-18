from sys import exit

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
			return next_room
		else:
			print "You can't go there."
		
class Death(Room):
	
	def __init__(self, name, desc):
		super(Death, self).__init__(self, name, desc)
	
	def enter(self):
		print self.desc
		exit(1)