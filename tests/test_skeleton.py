# -*- coding: utf-8 -*-

import pytest
from judo_python.skeleton import fib

__author__ = "David Lenwell"
__copyright__ = "David Lenwell"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
