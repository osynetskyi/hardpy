def convert_numbers(s):
	try:
		return int(s)
	except ValueError:
		return None
		
def convert_numbers2(s):
	digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	for char in s:
		if char not in digits:
			return None
	return int(s)
		
def scan(s):
	cases = {
		'direction': ['north', 'south', 'east', 'west', 'up', 'down'],
		'verb': ['go', 'kill', 'eat', 'take', 'show', 'equip', 'tell', 'place', 'shoot', 'dodge', 
				 'enter', 'ask', 'throw'],
		'stop': ['the', 'in', 'of', 'at', 'on', 'by'],
		'noun': ['bear', 'princess', 'sword', 'goblin', 'tower', 'joke', 'bomb', 'help', 'attack', 		   'gothon', 'pod', 'code']
	}
	res = []
	
	input = s.split(' ')
	for word in input:
		found = 0
		if convert_numbers(word) != None:
			res.append(('number', convert_numbers(word)))
			continue
		for k, v in cases.items():
			if word.lower() in v:
				res.append((k, word))
				found = 1
				break
		if found == 0:
			res.append(('error', word))
	return res