from sys import exit
from random import randint

class Character(object):
	
	def __init__(self, name, hp, min_atk, max_atk, min_def, max_def):
		self.name = name
		self.hp = hp
		self.min_atk = min_atk
		self.max_atk = max_atk
		self.min_def = min_def
		self.max_def = max_def

class Scene(object):
	
	def enter(self):
		print "The scene is not implemented yet."
		exit(1)
		
class Fight(Scene):
	
	def __init__(self, char1, char2):
		self.char1 = char1
		self.char2 = char2
		
	def enter(self):
		print self.char1.name, " vs ", self.char2.name
		while self.char1.hp > 0 and self.char2.hp > 0:
			your_dmg = 0
			your_def = self.char1.min_def
			enemy_dmg = 0
			enemy_def = self.char2.min_def
			
			action = raw_input("[battle]> ")
			if action == "attack":
				print "You're aiming at Gothon"
				your_dmg = randint(self.char1.min_atk, self.char1.max_atk)
			elif action == "dodge":
				print "You're covering from attack"
				your_def = randint(self.char1.min_def + 1, self.char1.max_def)
			
			enemy_choice = randint(0,1)
			if enemy_choice == 0:
				print "Gothon is aiming at you"
				enemy_dmg = randint(self.char2.min_atk, self.char2.max_atk)
			else:
				print "Gothon tries to evade the attack"
				enemy_def = randint(self.char2.min_def + 1, self.char2.max_def)
				
			if your_dmg - enemy_def > 0 :
				print "You hit Gothon for %d hp" % (your_dmg - enemy_def)
				self.char2.hp -= your_dmg - enemy_def
				
			if enemy_dmg - your_def > 0:
				print "Gothon hits you for %d hp" % (enemy_dmg - your_def)
				self.char1.hp -= enemy_dmg - your_def
				
		if self.char2.hp <= 0:
			print "You killed Gothon!"
			return 'back'
		elif self.char1.hp <= 0:
			print "Gothon killed you!"
			return 'death'
				
		

class Engine(object):
	
	enemies = {
		"central_corridor": Character("Gothon soldier", 5, 1, 2, 0, 3),
		"bridge_entrance": Character("Gothon captain", 8, 2, 4, 1, 4)
	}
	
	advance = {
		"central_corridor": "laser_weapon_armory",
		"bridge_entrance": "the_bridge"
	}
	
	def __init__(self, scene_map):
		self.map = scene_map
		
	def play(self):
		Player = Character("You", 10, 1, 5, 2, 6)
		last_scene = "finished"
		#scene = self.map.opening_scene()
		scene = 'central_corridor'
		while scene != last_scene:
			new_scene = self.map.next_scene(scene)
			if new_scene != 'fight':
				scene = new_scene
			else:
				fight = Fight(Player, self.enemies[scene])
				result = Fight.enter(fight)
				if result != 'back':
					scene = result
				else:
					scene = self.advance[scene]
		print "Congratulations, you win!"
		
class Death(Scene):
	
	jokes = [
		"You suck.",
		"Try harder.",
		"Lol."
	]
	
	def enter(self):
		print "You died."
		print self.jokes[randint(0, len(self.jokes) - 1)]
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		print "You're in central corridor.\nThere is a Gothon standing here."
		choice = raw_input("> ")
		if choice == "dodge":
			print "You failed to dodge Gothon."
			return 'death'
		elif choice == "shoot":
			print "You kill Gothon!"
			return 'laser_weapon_armory'
		elif choice == "attack":
			return 'fight'
		else:
			print "Gothon killed you."
			return 'death'
		
class LaserWeaponArmory(Scene):
	
	def enter(self):
		print "You're in the laser weapon armory.\nYou see a locker."
		code = "%d%d%d" % (randint(1, 9), randint(0, 9), randint(0, 9))
		choice = raw_input("> ")
		if choice == "open":
			print "You have 10 guesses to find the locker code."
			res = self.guess_code(code)
			if res:
				print "You open the locker, take the bomb and head to the bridge."
				return 'bridge_entrance'
			else:
				print "The lock mechanism is jammed. Eventually gothons find and kill you."
				return 'death'				
		else:
			print "Come again?.\n"
			return 'laser_weapon_armory'
			
	def guess_code(self, code):
		guess = ''
		tries = 10
		while tries > 0:
			print "Guess a number between 1 and 1000"
			guess = raw_input("[code]> ")
			if guess == code or guess == 'cheat':
				return True
			elif guess > code:
				print "Lower!"
			else:
				print "Higher!"
			tries -= 1
		return False

class BridgeEntrance(Scene):
	
	def enter(self):
		print "As you approach the bridge, you see a Gothon captain."
		choice = raw_input("> ")
		if choice == "attack":
			return 'fight'
		else:
			print "Gothon killed you."
			return 'death'
			
class TheBridge(Scene):

	def enter(self):
		print "You're on the bridge."
		print "Now that Gothon is dead you need to place the bomb."
		choice = raw_input("> ")
		if choice == "plant bomb":
			print "You carefully plant the bomb."
			return 'escape_pod'
		elif choice == "kick bomb":
			print "You kick the bomb and it blows!"
			return 'death'
		else:
			print "Come again?."
			return 'the_bridge'
		
class EscapePod(Scene):

	def enter(self):
		print "You reach escape pod bay. There are 5 pods here, some of which could be broken."
		good_pod = randint(1, 5)
		choice = raw_input("[pod #]> ")
		if choice == str(good_pod) or choice == 'cheat':
			print "You guessed right!"
			return 'finished'
		else:
			print "Wrong!"
			return 'death'
		
		
class Map(object):

	scenes = {
		"central_corridor": CentralCorridor(),
		"laser_weapon_armory": LaserWeaponArmory(),
		"death": Death(),
		"escape_pod": EscapePod(),
		"the_bridge": TheBridge(),
		"bridge_entrance": BridgeEntrance()
	}

	def __init__(self, start_scene):
		self.start = start_scene
		
	def next_scene(self, scene_name):
		return self.scenes[scene_name].enter()
		
	def opening_scene(self):
		return self.scenes[self.start].enter()
		
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()