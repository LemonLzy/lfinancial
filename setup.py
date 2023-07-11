from setuptools import setup, find_packages

excluded_packages = ["docs", "tests", "tests.*"]
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='lfinancial',
    version='0.2.8',
    author='zaneliu',
    description='Generate financial test data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    readme="README.md",
    author_email='lzy291980138@163.com',
    packages=find_packages(exclude=excluded_packages),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
    ],
)
