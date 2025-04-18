import os
from setuptools import setup

dirname = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(dirname, 'README.rst'), 'r') as infile:
    long_description = infile.read()

setup(
    name = 'mplstereonet',
    version = '0.6.3.post2',
    description = "Stereonets for matplotlib",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author = 'Joe Kington',
    author_email = 'joferkington@gmail.com',
    license = 'MIT',
    url = 'https://github.com/joferkington/mplstereonet/',
    packages = ['mplstereonet'],
    install_requires = [
        'matplotlib >= 3.9',
        'numpy >= 1.26']
)
