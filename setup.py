from setuptools import setup

excluded_packages = ["docs", "tests", "tests.*"]
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='lfinancial',
    version='0.0.6',
    author='zaneliu',
    description='Generate financial test data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    readme="README.md",
    author_email='lzy291980138@163.com',
    packages=['lfinancial'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
