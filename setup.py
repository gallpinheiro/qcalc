from setuptools import setup, find_packages

setup(
	name="qcalc",
	version="0.0.1",
	author="Gabriel, QTNano",
	author_email="galinslp@gmail.com",
	description="qcalc offers a command-line interface for automatize FHI-aims calculation.",
	url="https://google.com",
	entry_points = {
	'console_scripts': ['qcalc = qcalc.console:main'],},
	packages=find_packages(),
	classifiers=[
	"Programming Language :: Python :: 2.7",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
	],
	python_requires='>=2.7',
)
