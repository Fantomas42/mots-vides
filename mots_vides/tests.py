"""
Tests for mots-vides
"""
import os

from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader

import stopwords
import constants

constants.DATA_DIRECTORY = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)),
    'testdata/'
)

class StopWordFactoryTestCase(TestCase):

    factory = stopwords.StopWordFactory()
    language = 'foo'
    expection_file_collection = set(['bla', 'foo', 'bar', 'woot', 'doublewoot'])
    expected_filename = 'foo.txt'

    def _flush_cash(self):
        stopwords.LOADED_LANGUAGES.clear()

    def test_get_stopwords(self):
        sw = self.factory.get_stop_words(self.language, fail_safe=False)
        self.assertTrue(isinstance(sw, stopwords.StopWord))
        self.assertEqual(sw.collection, self.expection_file_collection)
        self._flush_cash()
        sw = self.factory.get_stop_words('blabla', fail_safe=True)
        self.assertEqual(len(sw), 0)
        with self.assertRaises(Exception):
            sw = factory.get_stop_words('blabla', fail_safe=False)

    def test_get_collection_filename(self):
        with self.assertRaises(IOError):
            self.factory.get_collection_filename('jkhj')

        filename = self.factory.get_collection_filename('jkhj')
        self.assertEqual(filename, self.expected_filename)




class StopWordTestCase(TestCase):

    collection_test1 = set(["foo", "bar", "bla"])
    collection_test2 = set(["oof", "rab", "alb"])

    def test_len_method(self):
        sw1 = stopwords.StopWord('foo', self.collection_test1)
        print "1"

        self.assertEqual(len(sw1), len(sw1.collection))

    def test_contain_method(self):
        sw1 = stopwords.StopWord('foo', self.collection_test1)
        print "2"
        for elem in self.collection_test1:
            self.assertTrue(elem in sw1)

    def test_iter_method(self):
        sw1 = stopwords.StopWord('foo', self.collection_test1)
        expected_item_count = 3
        count = 0
        for elem in sw1:
            count += 1
        print "3"
        self.assertEqual(expected_item_count, count)

    def test_add_n_sub_method(self):
        sw1 = stopwords.StopWord('foo', self.collection_test1)
        sw2 = stopwords.StopWord('bar', self.collection_test2)
        print "4"
        sw1 + sw2

        for elem in sw2.collection:
            self.assertTrue(elem in sw1.collection)

        sw1 - sw2

        for elem in sw2.collection:
            self.assertTrue(elem not in sw1.collection)


loader = TestLoader()

test_suite = TestSuite(
    [
        loader.loadTestsFromTestCase(StopWordTestCase),
    ]
)
