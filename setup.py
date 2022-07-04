from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup (
	name = 'tube-cast',
	description = 'tube-cast: A command-line program to convert YouTube videos to Podcasts',
	version = '0.0.5',
	install_requires = [
	    'click',
	    'scrapetube',
	    'yt_dlp',
	    'pyppeteer',
	    ],
	python_requires='>=3.7', # any python greater than 2.7
	entry_points='''
	       [console_scripts]
	       tube-cast=src.__main__:cli
	   ''',
	author="Abe Hanoka",
	keyword="python, cli, youtube, podcast",
    packages=find_packages(),
	long_description=long_description,
	long_description_content_type="text/markdown",
	license='MIT',
	url='https://github.com/abe-101/tube-cast',
	download_url='https://github.com/abe-101/tube-cast/releases/download/v0.0.5/tube-cast-0.0.5.tar.gz',
    author_email='abe@habet.dev',
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)
