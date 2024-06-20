from setuptools import setup, find_packages

setup(
    name="MandelbrotJulia",
    version="2.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    python_requires=">=3.11",
)