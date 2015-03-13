from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksProj4ToEPSG',
    version='0.0.9',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks Proj4 to EPSG code convert library',
    install_requires=[
        'watchdog',
        'flask',
        'flask-cors'
    ],
    url='http://pypi.python.org/pypi/GeobricksProj4ToEPSG/',
    keywords=['geobricks', 'proj4', 'epsg', 'gis', 'geo'],
    package_data={"": ["geobciks_proj4_to_epsg/data/*"]},
    include_package_data=True
)
