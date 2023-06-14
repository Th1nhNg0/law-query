from setuptools import setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lawquery",
    version="0.0.1",
    description="Query the law",
    package_dir={"": "src"},
    package_data={"": ["*.json.gz"]},
    include_package_data=True,
    long_description=long_description,
    url="https://github.com/Th1nhNg0/law-query",
    author="Th1nhNg0",
    author_email="thinhngow@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
