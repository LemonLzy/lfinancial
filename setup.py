from setuptools import find_packages, setup

excluded_packages = ["docs", "tests", "tests.*"]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='lfinancial',
    version='0.0.5',
    author='zaneliu',
    author_email='lzy291980138@163.com',
    description='Generate financial test data',
    packages=['lfinancial'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
