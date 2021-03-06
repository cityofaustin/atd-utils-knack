import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atd_knackutil",
    version="0.0.2",
    author="City of Austin",
    author_email="transportation.data@austintexas.gov",
    description="Python utilities for interacting with Knack applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cityofaustin/atd-utils-args",
    install_requires=[
        "arrow"
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", 
    ),
)

