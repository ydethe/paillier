# python-paillier [![Latest released version on PyPi](https://img.shields.io/pypi/v/phe.svg)](https://pypi.python.org/pypi/phe/)

[![CI Status](https://github.com/data61/python-paillier/actions/workflows/test.yml/badge.svg)](https://github.com/data61/python-paillier/actions/workflows/test.yml)
[![Documentation Status](https://readthedocs.org/projects/python-paillier/badge/?version=stable)](http://python-paillier.readthedocs.org/en/latest/?badge=stable)

A Python 3 library implementing the Paillier Partially Homomorphic
Encryption.

The homomorphic properties of the paillier crypto system are:

-   Encrypted numbers can be multiplied by a non encrypted scalar.
-   Encrypted numbers can be added together.
-   Encrypted numbers can be added to non encrypted scalars.

# Citing

[python-paillier]{.title-ref} is designed, developed and supported by
[CSIRO\'s Data61](https://www.data61.csiro.au/). If you use any part of
this library in your research, please cite it using the following BibTex
entry:

    @misc{PythonPaillier,
      author = {CSIRO's Data61},
      title = {Python Paillier Library},
      year = {2013},
      publisher = {GitHub},
      journal = {GitHub Repository},
      howpublished = {\url{https://github.com/data61/python-paillier}},
    }

## Running unit tests

    python setup.py test

Or use nose:

    nosetests

## Note related to gmpy2

gmpy2 is not required to use the library, but is
preferred. A pure Python implementation is available but
gmpy2 drastically improves performances. As indication on
a laptop not dedicated to benchmarking, running the example
[examples/federated_learning_with_encryption.py]{.title-ref} provided in
the library took: - 4.5s with gmpy2 installed - 35.7s
without gmpy2 installed

However, gmpy2 is a requirement to run the tests.

## Code History

Developed at [Data61 \| CSIRO](http://data61.csiro.au).

Parts derived from the Apache licensed Google project:
<https://code.google.com/p/encrypted-bigquery-client/>
