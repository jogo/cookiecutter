Usage
=====

Generate a Python package project::

    cookiecutter https://github.com/jogo/cookiecutter.git


Requirements
-------------

* working git repo (due to pbr and versioning, just run ``git init``)
* cookiecutter_ to setup repo
* tox_ to run tests

.. _cookiecutter: https://pypi.python.org/pypi/cookiecutter
.. _tox: https://pypi.python.org/pypi/tox

about
-----

Sets up the skeleton of a python project that uses the following packages

* testrepository_ to run tests
* pbr_  to build packages
* flake8_ for python linting
* tox_ 


.. _testrepository: https://pypi.python.org/pypi/testrepository
.. _flake8: https://pypi.python.org/pypi/flake8
.. _pbr: https://pypi.python.org/pypi/pbr
