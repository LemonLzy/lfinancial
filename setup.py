from setuptools import setup
from pathlib import Path

excluded_packages = ["docs", "tests", "tests.*"]
here = Path(__file__).resolve().parent
README = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='lfinancial',
    version='0.0.6',
    author='zaneliu',
    long_description=README,
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
