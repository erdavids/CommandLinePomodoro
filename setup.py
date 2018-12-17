from setuptools import setup

setup(
	name="pomodoro",
	version='1.1',
	author='Eric Davidson',
	py_modules=['pom'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		pomodoro=pom:main
	''',
)
