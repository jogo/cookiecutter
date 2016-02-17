"""
test_{{ cookiecutter.module_name }}
----------------------------------
Tests for `{{ cookiecutter.module_name }}` module.
"""

from {{ cookiecutter.module_name }}.tests import base


class Test{{ cookiecutter.module_name|capitalize }}(base.TestCase):

    def test_something(self):
        pass
