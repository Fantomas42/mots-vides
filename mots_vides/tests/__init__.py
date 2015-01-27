"""
Tests for mots-vides
"""
import os

from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader

from mots_vides import stop_words

from mots_vides import constants


class StopWordFactoryTestCase(TestCase):

    factory = stop_words.StopWordFactory(path=os.path.join(
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

        self.factory = stop_words.StopWordFactory()
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


class StopWordTestCase(TestCase):

    collection_test1 = set(["foo", "bar", "bla"])
    collection_test2 = set(["oof", "rab", "alb"])

    def test_len_method(self):
        sw1 = stop_words.StopWord('foo', self.collection_test1)
        self.assertEqual(len(sw1), len(sw1.collection))

    def test_contain_method(self):
        sw1 = stop_words.StopWord('foo', self.collection_test1)
        for elem in self.collection_test1:
            self.assertTrue(elem in sw1)

    def test_iter_method(self):
        sw1 = stop_words.StopWord('foo', self.collection_test1)
        expected_item_count = 3
        count = 0
        for elem in sw1:
            count += 1
        self.assertEqual(expected_item_count, count)

    def test_add_n_sub_method(self):
        sw1 = stop_words.StopWord('foo', self.collection_test1)
        sw2 = stop_words.StopWord('bar', self.collection_test2)
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
        loader.loadTestsFromTestCase(StopWordFactoryTestCase),
    ]
)
