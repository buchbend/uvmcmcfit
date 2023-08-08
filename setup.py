import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uvmcmcfit",
    version="1.0",
    author="Shane Bussman",
    author_email="b@b.de",
    description="bl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # project_urls={
    #     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    # },
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "astropy",
        "emcee",
        "matplotlib",
        "numpy",
        "pyyaml",
    ],
)
