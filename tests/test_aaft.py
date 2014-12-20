# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 10:54:20 2014

@author: eisenmanl
"""

from __future__ import (print_function, absolute_import,
                        unicode_literals, division)
import six

import numpy as np
import pytest

import aaft


class MockRandom():
    """
    use a list of random number from Octave for testing purposes
    """
    def __init__(self, file_name):
        self.index = 0
        self.values = np.loadtxt(file_name)
        self.max = len(self.values)

    def _rand(self):
        if self.index < self.max:
            val = self.values[self.index]
            self.index += 1
            return val
        else:
            raise ValueError("out of random values. index = %i" % (self.index))

    def rand(self, num=1):
        if num < 1:
            raise ValueError('num needs to be at least 1')
        if num == 1:
            return self._rand()

        result = np.zeros(num)
        for i in range(num):
            result[i] = self._rand()

        return result


@pytest.fixture
def phase():
    return np.loadtxt('tests/phase.csv', delimiter=',')


@pytest.fixture
def sur():
    return np.loadtxt('tests/sur.csv', delimiter=',')


class Testaaft():
    """ class for testing aaft"""

    mock_rand = MockRandom('tests/random.txt')
    mock_randn = MockRandom('tests/randomN.txt')

    def test_aaft(self, phase, sur, monkeypatch):
        monkeypatch.setattr(np.random, 'rand', self.mock_rand.rand)
        monkeypatch.setattr(np.random, 'randn', self.mock_randn.rand)
        aaft_sur = aaft.AAFTsur(phase)
        assert len(aaft_sur) == len(sur)
        assert np.allclose(aaft_sur, sur)
