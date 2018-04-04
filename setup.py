try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'This program removes the first line from CSV files, often the header row.  It opens every file with the `.csv` extension in the current working directory, reads in the contents and rewrites the contents without the first row...  all to a file of the same name.  This replaces the old contents of the CSV file with the new, headless content.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['csv'],
	'scripts': [],
	'name': 'Remove Header from CSV Files'
}

setup(**config)