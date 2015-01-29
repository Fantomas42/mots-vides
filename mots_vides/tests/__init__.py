"""
Tests for mots-vides
"""
from unittest import TestSuite
from unittest import TestLoader

from mots_vides.tests.stop_words import StopWordTestCase
from mots_vides.tests.stop_words import StopWordRebaseTestCase
from mots_vides.tests.factory import StopWordFactoryTestCase

loader = TestLoader()

test_suite = TestSuite(
    [
        loader.loadTestsFromTestCase(StopWordTestCase),
        loader.loadTestsFromTestCase(StopWordRebaseTestCase),
        loader.loadTestsFromTestCase(StopWordFactoryTestCase),
    ]
)
