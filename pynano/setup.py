"""Setup for the pynano package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="J.A. Sampedro",
    author_email="techurbana@gmail.com",
    name='pynano',
    license="MIT",
    description='Arduino + pyFirmata.',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/techurbana/pynano',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
