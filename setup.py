import sys

from setuptools import setup
from setuptools import find_packages

version = '0.1'

install_requires = [
    'discord.py',
    'aiohttp'
]

setup(
    name='bonobot',
    version=version,
    description="Server and bot for discord",
    author='L2pAcademy',
    author_email='dev@L2p-academy.fr',
    license='GPL-v3',
    packages=find_packages(),
    install_requires=install_requires
)
