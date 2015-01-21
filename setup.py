"""Setup script of mots-vides"""
from setuptools import setup
from setuptools import find_packages

import mots_vides

setup(
    name='mots-vides',
    version=mots_vides.__version__,

    description='Python library for managing stop words in many languages.',
    long_description=open('README.rst').read(),
    keywords='stop, words, text, parsing',

    author=mots_vides.__author__,
    author_email=mots_vides.__email__,
    url=mots_vides.__url__,

    license=open('LICENSE').read(),

    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules']
)
