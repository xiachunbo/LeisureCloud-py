#!/usr/bin/env python
# coding=utf-8
import setuptools
from setuptools import setup

'''
把服务打包成Scripts下的exe文件
'''

setup(
    name="leisure",  #pypi中的名称，pip或者easy_install安装时使用的名称，或生成egg文件的名称
    version="1.0",
    author="xiaobobo",
    author_email="853233432@qq.com",
    description=("This is a service"),
    license="v1",
    keywords="leisure",
    url="",
    packages= setuptools.find_packages(),  # 需要打包的目录列表 setuptools.find_packages(),

    # 需要安装的依赖
    install_requires=[
        'redis>=2.10.5',
        'setuptools>=16.0',
    ],

    # 添加这个选项，在windows下Python目录的scripts下生成exe文件
    # 注意：模块与函数之间是冒号:
    entry_points={'console_scripts': [
        'leisure_run = leisure.main:main',
    ]},

    # long_description=read('README.md'),
    classifiers=[  # 程序的所属分类列表
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    # 此项需要，否则卸载时报windows error
    zip_safe=False
)