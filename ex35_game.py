from sys import exit

has_key = False
has_sword = False
		
def sphinx_room():
	print "There is a great sphinx in this room. As you approach it, his eyes open and you hear the voice:"
	print "'Answer my riddle, mortal, and you will be granted passage. Fail, and I'll take your life.'"
	print "'What is it that walks on four legs in the morning, two in afternoon and three in evening?'"
	
	answer = raw_input("> ")
	
	if answer == "human":
		print "'You are correct, mortal. You may pass.'"
		print "The sphinx disappears and you see a small key on his pedestal. What do you do?"
		
		while True:
		
			choice = raw_input("> ")
		
			if choice == "take key":
				global has_key
				has_key = True
				print "You pocket the small key and return to the hall."
				start()
			else:
				print "What do you mean, %s?" % choice
		
	else:
		print "'You are wrong. Now face the consequences.'"
		dead("Sphinx leaps on you and smashes your head off")

def trap_room():
	print "You enter a dark room. The silence here is almost terrifying."
	print "Suddenly, a spear is launched from the opposite wall and flies at you!"
	print "Do you dodge or catch it?"
	
	choice = raw_input("> ")
	
	if choice == "dodge":
		print "You manage to evade the spear!"
	elif choice == "catch":
		print "You try to catch the spear, but it's moving too fast."
		dead("The spear pierces your chest and you die.")
	else:
		print "While you thinking the spear gets very close and its too late."
		dead("The spear pierces your chest and you die.")
	
	print "Having escaped a certain death, you see a small door here. What do you do?"
	while True:
		choice = raw_input("> ")
		
		if choice == "open door" and has_key:
			print "You open the door and venture forward."
			sword_room()
		elif choice == "open door" and not has_key:
			print "You'll need the key to unlock this. You head back hoping to find one."
			start()
		else:
			print "This isn;t going to work."

def sword_room():
	print "You enter a small room. The ray of sunlight is shining through the ceiling and in this ray you see a shiny sword in stone."
	print "What do you do?"
	
	while True:
		choice = raw_input("> ")
	
		if choice == "take sword":
			global has_sword
			has_sword = True
			print "You wield the sword and head back."
			start()
		else:
			print "I have no idea what that means."
	
def ogre_room():
	print "There is a giant angry ogre here."
	print "The ogre notices you, growls and starts running in your direction."
	print "Do you fight him or retreat?"
	ogre_dead = False
	
	choice = raw_input("> ")
	
	if choice == "retreat":
		print "You flee back to the hall and shut the door."
		start()
	elif choice == "fight":
		if has_sword:
			print "You strike the ogre down with your shiny sword."
			ogre_dead = True
		else:
			print "You try to hit an ogre with your fist, but he doesn't seem to notice it."
			dead("The ogre bites your head off.")
	
	if ogre_dead:
		print "Now the ogre lies dead and you can see a door at the other side of the room."
		print "What do you do?"
		
		while True:
			choice = raw_input("> ")
		
			if choice == "open door":
				print "You open the door and head into next room."
				treasure_room()
			else:
				print "Wait, what?"

def treasure_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	#if "0" in choice or "1" in choice:
	if choice.isdigit():	
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
	
	if how_much < 100:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

		
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a hall with three doors - one is on the left side, other is on the right, and third one is in front of you."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		ogre_room()
	elif choice == "right":
		trap_room()
	elif choice == "front":
		sphinx_room()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()