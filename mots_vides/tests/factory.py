"""
Tests for StopWordFactory
"""
import os
from unittest import TestCase

from mots_vides.factory import StopWordFactory


class StopWordFactoryTestCase(TestCase):

    factory = StopWordFactory(path=os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)),
            'datas/'
        )
    )
    language = 'foo'
    expection_file_collection = set(['bla', 'foo', 'bar',
                                     'woot', 'doublewoot'])
    expected_filename = 'foo.txt'

    def _flush_cash(self):
        stop_words.LOADED_LANGUAGES.clear()

    def test_get_stopwords(self):
        sw = self.factory.get_stop_words(self.language)
        self.assertTrue(isinstance(sw, stop_words.StopWord))
        self.assertEqual(sw.collection, self.expection_file_collection)
        self._flush_cash()

        sw = self.factory.get_stop_words('blabla', fail_safe=True)
        self.assertEqual(len(sw), 0)
        self._flush_cash()

        self.factory = StopWordFactory()
        self.assertRaises(
            Exception,
            lambda: self.factory.get_stop_words,
            'blabla'
        )

    def test_get_collection_filename(self):
        self.assertRaises(
            Exception,
            lambda: self.factory.get_collection_filename,
            'jkhj'
        )
        filename = self.factory.get_collection_filename('foo')
        self.assertEqual(filename, self.expected_filename)
