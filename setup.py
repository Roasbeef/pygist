import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

dependencies = ['clint2', 'requests']

setup(
    name='pygist',
    version='0.2',
    description='a simple cli for interacting with github gists',
    url='https://github.com/Roasbeef/pygist',
    author='Olaoluwa Osuntokun',
    author_email='laolu32@gmail.com',
    install_requires=dependencies,
    packages=['pygist', ],
    license='MIT License',
    long_description=open('README.txt').read(),
    entry_points={
        'console_scripts': [
            'pygist = pygist.cli:begin',
        ],
    },
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
    ),
    )
