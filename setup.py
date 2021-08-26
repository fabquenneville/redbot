#!/usr/bin/env python3

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redbot",
    version="0.0.1",
    author="Fabrice Quenneville",
    author_email="fab@fabq.ca",
    url="https://github.com/fabquenneville/redbot",
    download_url="https://pypi.python.org/pypi/redbot",
    project_urls={
        "Bug Tracker": "https://github.com/fabquenneville/redbot/issues",
        "Documentation": "https://fabquenneville.github.io/redbot/",
        "Source Code": "https://github.com/fabquenneville/redbot",
    },
    description="redbot is a Python command line tool to take some actions on reddit automatically.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Topic :: Communications :: Video :: Conversion",
        "Development Status :: 1 - Planning",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    entry_points = {
        'console_scripts': ['redbot=redbot.redbot:main'],
    },
    keywords=[
        "social", "reddit", "automatic"
    ],
    install_requires=[
        "configparser", "praw", "sqlite3"
    ],
    license='GPL-3.0',
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=True,
)