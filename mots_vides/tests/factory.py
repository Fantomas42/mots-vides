"""
Tests for StopWordFactory
"""
import os

from unittest import TestCase

from mots_vides.stop_words import StopWord
from mots_vides.factory import StopWordFactory
from mots_vides.exceptions import StopWordError


class StopWordFactoryTestCase(TestCase):

    def setUp(self):
        self.data_directory = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)),
            'datas/')
        self.factory = StopWordFactory(self.data_directory)

    def test_get_stopwords(self):
        sw = self.factory.get_stop_words('foo')
        self.assertTrue(isinstance(sw, StopWord))
        self.assertEqual(list(sw.collection),
                         ['bla', 'foo', 'bar',
                          'woot', 'doublewoot'])

        sw = self.factory.get_stop_words('blabla', fail_safe=True)
        self.assertEqual(len(sw), 0)

        self.factory = StopWordFactory()
        self.assertRaises(StopWordError, self.factory.get_stop_words, 'blabla')

    def test_get_collection_filename(self):
        filename = self.factory.get_collection_filename('foo')
        self.assertTrue(filename.endswith('foo.txt'))
        self.assertTrue(filename.startswith(self.data_directory))
