from nose.tools import *
from ex48.parser import *

'''def test_peek():
	assert_equal(parser.peek([('verb', 'eat'), ('noun', 'bat'), ('error', 'sdfsdf')]), 'verb')
	assert_equal(parser.peek([('error', 'sdfsdgsdg'), ('noun', 'bat'), ('error', 'sdfsdf')]), 'error')
	assert_equal(parser.peek([]), None)

def test_match():
	assert_equal(parser.match([('verb', 'eat'), ('noun', 'bat'), ('error', 'sdfsdf')], 
							  'verb'), 
				 ('verb', 'eat'))
	assert_equal(parser.match([('direction', 'south'), ('noun', 'bat'), ('error', 'sdfsdf')], 
							  'direction'), 
				 ('direction', 'south'))
	assert_equal(parser.match([('verb', 'eat'), ('noun', 'bat'), ('error', 'sdfsdf')], 
							  'noun'), 
				 None)
	assert_equal(parser.match([], 'verb'), None)				 

def test_parse_verb():
	assert_equal(parser.parse_verb([('verb', 'eat'), ('stop', 'in'), ('stop', 'at')]), ('verb', 'eat'))
	assert_equal(parser.parse_verb([('error', 'safsd'), ('stop', 'in'), ('stop', 'at'), ('verb', 'kill')]), ('verb', 'kill'))
	assert_equal(parser.parse_verb([('error', 'safsd'), ('error', 'asat'), ('verb', 'kill')]), ('verb', 'kill'))
	assert_equal(parser.parse_verb([('stop', 'in'), ('error', 'asat'), ('verb', 'kill')]), ('verb', 'kill'))
	assert_raises(parser.ParserError, parser.parse_verb, [('stop', 'in'), ('stop', 'at'), ('noun', 'bear')])
	
def test_parse_number():
	assert_equal(parser.parse_number([('number', 123), ('stop', 'in'), ('stop', 'at')]), ('number', 123))
	assert_equal(parser.parse_number([('stop', 'in'), ('error', 'asdat'), ('number', 123)]), ('number', 123))
	assert_equal(parser.parse_number([('noun', 'bat'), ('stop', 'in'), ('stop', 'at')]), ('number', 1))
	
def test_parse_object():
	assert_equal(parser.parse_object([('noun', 'princess'), ('stop', 'in'), ('stop', 'at')]), ('noun', 'princess'))
	assert_equal(parser.parse_object([('stop', 'in'), ('stop', 'at'), ('noun', 'sword')]), ('noun', 'sword'))
	assert_equal(parser.parse_object([('direction', 'up'), ('stop', 'in'), ('stop', 'at')]), ('direction', 'up'))
	assert_equal(parser.parse_object([('stop', 'in'), ('stop', 'at'), ('direction', 'down')]), ('direction', 'down'))
	assert_raises(parser.ParserError, parser.parse_object, [('stop', 'in'), ('stop', 'at'), ('verb', 'eat')])

def test_parse_subject():
	assert_equal(parser.parse_subject([('noun', 'princess'), ('stop', 'in'), ('stop', 'at')]), ('noun', 'princess'))
	assert_equal(parser.parse_subject([('stop', 'in'), ('stop', 'at'), ('noun', 'sword')]), ('noun', 'sword'))
	assert_equal(parser.parse_subject([('verb', 'take'), ('stop', 'in'), ('stop', 'at')]), ('noun', 'player'))
	assert_equal(parser.parse_subject([('stop', 'in'), ('stop', 'at'), ('verb', 'use')]), ('noun', 'player'))
	assert_raises(parser.ParserError, parser.parse_subject, [('stop', 'in'), ('stop', 'at'), ('direction', 'south')])
	
def test_parse_sentence():
	assert_equal(parser.parse_sentence([('noun', 'princess'), ('stop', 'in'), ('stop', 'at'), ('verb', 'wear'), ('error', 'shiny'), ('noun', 'dress')]).subject, 'princess')
	assert_equal(parser.parse_sentence([('noun', 'princess'), ('stop', 'in'), ('stop', 'at'), ('verb', 'wear'), ('error', 'shiny'), ('noun', 'dress')]).verb, 'wear')
	assert_equal(parser.parse_sentence([('noun', 'princess'), ('stop', 'in'), ('stop', 'at'), ('verb', 'wear'), ('error', 'shiny'), ('noun', 'dress')]).number, 1)
	assert_equal(parser.parse_sentence([('noun', 'princess'), ('stop', 'in'), ('stop', 'at'), ('verb', 'wear'), ('error', 'shiny'), ('noun', 'dress')]).object, 'dress')
	assert_equal(parser.parse_sentence([('stop', 'in'), ('stop', 'at'), ('verb', 'go'), ('error', 'shiny'), ('number', 2), ('stop', 'of'), ('direction', 'east')]).subject, 'player')
	assert_equal(parser.parse_sentence([('stop', 'in'), ('stop', 'at'), ('verb', 'go'), ('error', 'shiny'), ('number', 2), ('stop', 'of'), ('direction', 'east')]).verb, 'go')
	assert_equal(parser.parse_sentence([('stop', 'in'), ('stop', 'at'), ('verb', 'go'), ('error', 'shiny'), ('number', 2), ('stop', 'of'), ('direction', 'east')]).number, 2)
	assert_equal(parser.parse_sentence([('stop', 'in'), ('stop', 'at'), ('verb', 'go'), ('error', 'shiny'), ('number', 2), ('stop', 'of'), ('direction', 'east')]).object, 'east')'''
	
def test_parser1():
	sentence = Parser("princess go 2 north").sentence
	assert_equal(sentence.subject, "princess")
	assert_equal(sentence.verb, "go")
	assert_equal(sentence.number, 2)
	assert_equal(sentence.object, "north")
	
def test_parser2():
	sentence = Parser("at sdhjfk sa in kill of asf bear").sentence
	assert_equal(sentence.subject, "player")
	assert_equal(sentence.verb, "kill")
	assert_equal(sentence.number, 1)
	assert_equal(sentence.object, "bear")
	
def test_parser3():
	assert_raises(ParserError, Parser, "go kill 3")