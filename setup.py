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
    keywords='chartkra',         # 关键字
    author='Kazaf Chen',                               # 作者
    author_email='kazaf.chen@gmail.com',                # 邮箱
    url='https://github.com/KazafChen',      # 包含包的项目地址
    license='MIT',                                  # 授权方式
    packages=find_packages(),                       # 包列表
    include_package_data=True,
    zip_safe=True,
)