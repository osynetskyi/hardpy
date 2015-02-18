import lexicon

class ParserError(Exception):
	pass
	
class Sentence(object):
	
	def __init__(self, subject, verb, num, obj):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.number = num[1]
		self.object = obj[1]

class Parser(object):

	def __init__(self, input):
		self.word_list = lexicon.scan(input)
		self.sentence = self.parse_sentence()

	def peek(self):
		if self.word_list:
			word = self.word_list[0]
			return word[0]
		else:
			return None
			
	def match(self, expecting):
		if self.word_list:
			word = self.word_list.pop(0)
		
			if word[0] == expecting:
				return word
			else:
				return None
		else:
			return None
		
	def skip(self, word_types):
		while self.peek() in word_types:
			self.match(self.peek())
			
	def parse_verb(self):
		self.skip(['stop', 'error'])
	
		if self.peek() == 'verb':
			return self.match('verb')
		else:
			raise ParserError("Expected a verb next.")
		
	def parse_number(self):
		self.skip(['stop', 'error'])
	
		if self.peek() == 'number':
			return self.match('number')
		else:
			return ('number', 1)
	
	def parse_object(self):
		self.skip(['stop', 'error'])
		next_word = self.peek()
	
		if next_word == 'noun':
			return self.match('noun')
		elif next_word == 'direction':
			return self.match('direction')
		else:
			raise ParserError("Expected a noun or direction next.")
			
	def parse_subject(self):
		self.skip(['stop', 'error'])
		next_word = self.peek()
	
		if next_word == 'noun':
			return self.match('noun')
		elif next_word == 'verb':
			return ('noun', 'player')
		else:
			raise ParserError("Expected a verb next.")
			
	def parse_sentence(self):
		subj = self.parse_subject()
		verb = self.parse_verb()
		num = self.parse_number()
		obj = self.parse_object()
		return Sentence(subj, verb, num, obj)