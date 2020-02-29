"""The setup script."""

from setuptools import setup, find_packages
import os

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'buku==4.1',
    'requests==2.21.0',
    'ConfigArgParse==0.14.0'
]

setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest', ]

setup(
    author="Mike John",
    author_email='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Symmetrical sync between pocket and buku",
    install_requires=requirements,
    entry_points={
        "console_scripts": ['pokuz = pokuz.pokuz:main']
    },
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords='pokuz',
    name='pokuz',
    packages=find_packages(include=['pokuz']),
    setup_requires=setup_requirements,
    # test_suite='tests',
    # tests_require=test_requirements,
    url='https://github.com/ilovejs/pokuz',
    version='1.0',
    zip_safe=False,
)