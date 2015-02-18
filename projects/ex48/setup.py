try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'description',
	'author': 'author',
	'url': 'URL to get at it.',
	'download_url': 'Where to download it.',
	'author_email': 'mail',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'ex48'
}

setup(**config)