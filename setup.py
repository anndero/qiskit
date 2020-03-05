# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import os
import inspect
import setuptools
import sys


requirements = [
    "numpy>=1.13",
    "qiskit-terra>=0.8.0",
    "scipy>=0.19,!=0.19.1",
    "setuptools>=40.1.0",
]


if not hasattr(setuptools,
               'find_namespace_packages') or not inspect.ismethod(
                    setuptools.find_namespace_packages):
    print("Your setuptools version:'{}' does not support PEP 420 "
          "(find_namespace_packages). Upgrade it to version >='40.1.0' and "
          "repeat install.".format(setuptools.__version__))
    sys.exit(1)

requirements = [
    "qiskit-terra==0.12.0",
    "qiskit-aer==0.4.1",
    "qiskit-ibmq-provider==0.5.0",
    "qiskit-ignis==0.2.0",
    "qiskit-aqua==0.6.4",
]

setup(
    name="qiskit",
    version="0.16.1",
    description="Software for developing quantum computing programs",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/Qiskit/qiskit",
    author="Qiskit Development Team",
    author_email="qiskit@qiskit.org",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    packages=setuptools.find_namespace_packages(exclude=['test*']),
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5",
    zip_safe=False
)
