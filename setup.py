#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'aioworkers',
    'asynqp',
]

test_requirements = [
    'pytest',
]

setup(
    name='aioworkers-amqp',
    version='0.1.1',
    description="Module for working with amqp broker",
    author="Alexander Malev",
    author_email='yttrium@somedev.ru',
    url='https://github.com/aioworkers/aioworkers-amqp',
    packages=[i for i in find_packages() if i.startswith('aioworkers_amqp')],
    install_requires=requirements,
    license="Apache Software License 2.0",
    keywords='aioworkers amqp rabbitmq',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
