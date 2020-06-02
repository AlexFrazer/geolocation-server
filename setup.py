#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md', encoding='utf8') as f:
    readme = f.read()

setup(
    name='geolocation',
    version='0.0.0',
    author='Alex Frazer',
    author_email='frazer@alexfrazer.dev',
    license='BSD',
    description='Basic geolocation app',
    long_description=readme,
    zip_safe=False,
    python_requires='>=3.7',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
      'Flask',
      'requests',
    ],
    entry_points = {
      'console_scripts': [
        'app = app.cli:main',
      ],
    },
)