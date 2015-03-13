from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksCommon',
    version='0.0.6',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks common library.',
    install_requires=[
        'watchdog',
        'flask',
        'flask-cors',
        'requests'
    ],
    url='http://pypi.python.org/pypi/GeobricksCommon/',
    keywords=['geobricks']
)
