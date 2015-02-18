from nose.tools import *
from epicdungeon.rooms import Room

def test_room():
	gold = Room("GoldRoom",
				"""This room has gold in it you can grab. There's a
				door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.adjacent, {})
	assert_equal(gold.monsters, [])
	assert_equal(gold.items, [])
		
def test_go():
	
	center = Room("center", "Test room in the center.")
	north = Room("north", "Test room in the north.")
	south = Room("south", "Test room in the south.")
	
	center.adjacent = {"north": 'north', "south": 'south'}
	north.adjacent = {"south": 'center'}
	south.adjacent = {"north": 'center'}
	
	assert_equal(center.go('north'), 'north')
	assert_equal(center.go('south'), 'south')
	