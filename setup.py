"""Setup script of mots-vides"""
from setuptools import setup
from setuptools import find_packages

setup(
    name='mots-vides',
    version='2015.2.6',

    description='Python library for managing stop words in many languages.',
    long_description=open('README.rst').read(),
    keywords='stop, words, text, parsing',

    author='Fantomas42',
    author_email='fantomas42@gmail.com',
    url='https://github.com/Fantomas42/mots-vides',

    license=open('LICENSE').read(),

    packages=find_packages(),
    package_data={
        'mots_vides': [
            'datas/*.txt',
            ]
    },

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    entry_points={
        'console_scripts': [
            'merge-stop-words=mots_vides.scripts.merger:cmdline',
            'rebase-stop-words=mots_vides.scripts.rebaser:cmdline',
        ]
    }
)
