from nose.tools import *
from bin.app import *
from tests.tools import assert_response
cookie = ''

def test_cookie():

	resp = app.request("/", method="GET")
	global cookie
	cookie = resp.headers['Set-Cookie']
	
'''def test_signup():

	resp = app.request("/signup", method="GET", headers = {'Cookie': cookie})
	resp = app.request("/signup", method="POST", data={'user': 'sasha3', 'passwd': '123'}, headers = {'Cookie': cookie})'''

def test_login():

	resp = app.request("/login", method="GET", headers = {'Cookie': cookie})
	resp = app.request("/login", method="POST", data={'user': 'sasha3', 'passwd': '123'}, headers = {'Cookie': cookie})
	resp = app.request("/game", method="GET", headers = {'Cookie': cookie})
	assert_response(resp, contains="Corridor")

def test_game():
	
	app.request('/game', method='POST', data={'action': 'tell a joke'}, headers = {'Cookie': cookie})
	resp = app.request("/game", method="GET", headers = {'Cookie': cookie})
	assert_response(resp, contains="Laser Weapon")
	
	app.request('/game', method='POST', data={'action': '132'}, headers = {'Cookie': cookie})
	resp = app.request("/game", method="GET", headers = {'Cookie': cookie})
	assert_response(resp, contains="Bridge")
	
	app.request('/game', method='POST', data={'action': 'slowly place the bomb'}, headers = {'Cookie': cookie})
	resp = app.request("/game", method="GET", headers = {'Cookie': cookie})
	assert_response(resp, contains="Escape Pod")
	
	app.request('/game', method='POST', data={'action': '2'}, headers = {'Cookie': cookie})
	resp = app.request("/game", method="GET", headers = {'Cookie': cookie})
	assert_response(resp, contains="The End")
	
def test_logout():
	
	resp = app.request("/logout", method="GET", headers = {'Cookie': cookie})
	resp = app.request("/login", method="GET", headers = {'Cookie': cookie})
	assert_response(resp, contains="it's free!")	