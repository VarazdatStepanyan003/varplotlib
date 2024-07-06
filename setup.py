from setuptools import setup, find_packages

VERSION = '0.0.3'

setup(
    name="varplotlib",
    version=VERSION,
    author="VarazdatStepanyan003",
    description="Var's library for plotting data from various sources",
    long_description="I am lazy af",
    packages=find_packages(include=['varplotlib', 'varplotlib.*']),
    install_requires=["matplotlib"],
    keywords=["Varazdat", "plot", "matplotlib"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
    ]
)
