from setuptools import setup
setup(
    name='dockerdemo',
    version='0.1',
    packages=['dockerdemo',],
    entry_points = {
        'console_scripts': ['server=dockerdemo.main:main'],
    }
)