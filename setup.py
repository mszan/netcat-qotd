from setuptools import setup

setup(
    name = 'netcat-qotd',
    version = '0.1.0',
    packages = ['src'],
    install_requires= [
        'click'
    ],
    entry_points = {
        'console_scripts': [
            'netcat-qotd = src.__main__:main'
        ]
    })