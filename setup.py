from setuptools import setup


setup(
    name="lawquery",
    version="0.0.2",
    description="Query Vietnamese law documents",
    package_dir={"": "src"},
    package_data={"": ["*.json.gz"]},
    include_package_data=True,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
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
