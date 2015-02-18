import web
web.config.debug = False

urls = (
	'/login', 'Login',
	'/logout', 'Logout',
	'/signup', 'Signup'
)
app = web.application(urls, locals())
db = web.database(dbn='mysql', db='lpthw', user='root', pw='1qazXSW@3edc')

store = web.session.DiskStore('sessions')
session = web.session.Session(app, store,
                              initializer={'login': None})
							  
render = web.template.render('templates/', base="layout")
		
class Login:

	def GET(self):
		if session.login:
			return '%s' % render.login_ok(login=session.login)
		else:
			return '%s' % render.login()

	def POST(self):
		input = web.input(name=None, passwd=None)
		ident = db.select('users', where="login=$input['user']", vars=locals())[0]
		try:
			if input['passwd'] == ident['passwd']:
				session.login = input['user']
				return render.login_ok(login=session.login)
			else:
				session.login = None
				return render.error()
		except:
			session.login = None
			return render.error()
			
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
		
if __name__ == "__main__":
	app.run()