"""
Tests for mots-vides
"""
from unittest import TestCase
from unittest import TestSuite
from unittest import TestLoader

from mots_vides import stop_words


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
