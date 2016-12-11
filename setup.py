from setuptools import setup
import os

curdir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(curdir, "README.rst"), 'r') as readme:
	long_description = readme.read()

setup(
	name = "array2latex",
	version = "0.3",
	description = "A tool to convert array into latex tables",
	long_description = long_description,
	url = "https://github.com/adonese/arraytolatex",
	author = "Mohamed Yousif",
	author_email = "mmbusif@gmail.com",
	license = "MIT"
	)
