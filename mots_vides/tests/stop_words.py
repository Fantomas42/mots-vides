"""
Tests for mots-vides
"""
from unittest import TestCase

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

    def test_stopword_rebase_first(self):
        #test with first word in text
        sw1 = stop_words.StopWord('foo', set(["comme"]))
        text = "Comme je viens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "je viens de te le dire")

    def test_stopword_rebase_middle(self):
        #test with word in middle of text
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["viens"])
        text = "Comme je viens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme je de te le dire")

    def test_stopword_rebase_newline_between(self):
        #test with newline between two words
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["viens", "je"])
        text = "Comme je\nviens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme\nde te le dire")

    def test_stopword_rebase_newline_after(self):
        #test with newline after word
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["je"])
        text = "Comme je\nviens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme\nviens de te le dire")

    def test_stopword_rebase_newline_before(self):
        #test with newline before word
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["viens"])
        text = "Comme je\nviens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme je\nde te le dire")

    def test_stopword_rebase_two_escape_code_before(self):
        #test with newline before word
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["viens"])
        text = "Comme je\n\tviens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme je\n\tde te le dire")

    def test_stopword_rebase_two_escape_code_after(self):
        #test with newline before word
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["viens"])
        text = "Comme je viens\n\tde te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme je\n\tde te le dire")


    def test_stopword_rebase_tab_between(self):
        #test with newline between two words
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["viens", "je"])
        text = "Comme je\tviens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme\tde te le dire")

    def test_stopword_rebase_tab_after(self):
        #test with newline after word
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["je"])
        text = "Comme je\tviens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme\tviens de te le dire")

    def test_stopword_rebase_tab_before(self):
        #test with newline before word
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["viens"])
        text = "Comme je\tviens de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme je\tde te le dire")

    def test_stopword_dont_rebase(self):
        #test with newline before word
        sw1 = stop_words.StopWord('foo')
        sw1.collection = set(["viens"])
        text = "Comme je viensbhgfds de te le dire"
        text = sw1.rebase(text)
        self.assertEqual(
            text,
            "Comme je viensbhgfds de te le dire")
