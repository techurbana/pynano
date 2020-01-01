import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynano",
    version="0.0.1",
    author="J.A. Sampedro",
    author_email="techurbana@gmail.com",
    description="Arduino Nano + pyFirmata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/techurbana/pynano",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 
