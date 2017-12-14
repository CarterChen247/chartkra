# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

__author__ = 'Kazaf Chen'
__date__ = '2017/12/14'


setup(
    name='chartkra',
    version='0.0.5',
    description='chartkra',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords='chartkra',        
    author='Kazaf Chen',                   
    author_email='kazaf.chen@gmail.com',   
    url='https://github.com/KazafChen',    
    license='MIT',                         
    packages=find_packages(),              
    include_package_data=True,
    zip_safe=True,
)