"""
Tests for StopWordFactory
"""
import os

from unittest import TestCase

from mots_vides.stop_words import StopWord
from mots_vides.factory import StopWordFactory


class StopWordFactoryTestCase(TestCase):

    def setUp(self):
        self.data_directory = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)),
            'datas/')
        self.factory = StopWordFactory(self.data_directory)

    def test_get_stopwords(self):
        sw = self.factory.get_stop_words('klingon')
        self.assertTrue(isinstance(sw, StopWord))
        self.assertEqual(list(sw.collection),
                         ['nuq', "HIja'", "ghobe'", 'naDev'])

    def test_get_collection_filename(self):
        filename = self.factory.get_collection_filename('foo')
        self.assertTrue(filename.endswith('foo.txt'))
        self.assertTrue(filename.startswith(self.data_directory))
