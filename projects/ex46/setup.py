try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Project created while working on 46th excercise of "Learn Python The Hard Way"',
	'author': 'Oleksandr Synetskyi',
	'url': 'URL to get at it.',
	'download_url': 'Where to download it.',
	'author_email': 'alexander.sinetskiy@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex46'],
	'scripts': [],
	'name': 'ex46'
}

setup(**config)