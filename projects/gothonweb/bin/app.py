import web
from gothonweb import map
from gothonweb import parser

urls = (
	'/game', 'GameEngine',
	'/', 'Index',
	'/login', 'Login',
	'/logout', 'Logout',
	'/signup', 'Signup'
)

app = web.application(urls, globals())
db = web.database(dbn='mysql', db='lpthw', user='root', pw='1qazXSW@3edc')

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, 
								  {'room': None, 'login': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")

class Index(object):
	def GET(self):
		if session.login:
			web.seeother('/game')
		else:
			web.seeother('/login')
		
class Login:
	def GET(self):
		if session.login:
			session.room = map.START
			web.seeother('/game')
		else:
			return '%s' % render.login()

	def POST(self):
		input = web.input(name=None, passwd=None)
		ident = db.select('users', where="login=$input['user']", vars=locals())[0]
		try:
			if input['passwd'] == ident['passwd']:
				session.login = input['user']
				session.room = map.START
				web.seeother('/game')
			else:
				session.login = None
				return render.error()
		except:
			session.login = None
			return render.error()

class Signup:
	def GET(self):
		return render.signup()
		
	def POST(self):
		input = web.input(name=None, passwd=None)
		ident = db.select('users', where="login=$input['user']", vars=locals())
		if ident:
			return render.error()
		else:
			res = db.insert("users", login=input['user'], passwd=input['passwd'])
		return render.signup_ok()
		
class Logout:
	def GET(self):
		session.logged = 0
		session.kill()
		web.seeother('/login')
		
class GameEngine(object):

	def GET(self):
		if session.room:
			return render.show_room(room=session.room, help=None)
		else:
			web.seeother('/login')
		
	def POST(self):
		form = web.input(action=None)
		
		# there is a bug here, can you fix it?
		if session.room and form.action:
			if form.action == 'ask help':
				return render.show_room(room=session.room, help=session.room.help())
			else:
				session.room = session.room.go(form.action)
		
		web.seeother('/game')
		
if __name__ == "__main__":
	app.run()