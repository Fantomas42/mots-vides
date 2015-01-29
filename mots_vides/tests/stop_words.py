"""
Tests for StopWord
"""
from unittest import TestCase

from mots_vides.stop_words import StopWord


class StopWordTestCase(TestCase):

    def setUp(self):
        self.sw = StopWord('foo', ['foo', 'bar', 'baz'])

    def test_len(self):
        self.assertEqual(len(self.sw), 3)

    def test_contains(self):
        self.assertTrue('foo' in self.sw)
        self.assertFalse('qux' in self.sw)

    def test_iter(self):
        self.assertEqual(len(list(self.sw)), 3)

    def test_add(self):
        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw = nsw + self.sw
        self.assertEqual(sorted(list(nsw)),
                         ['bar', 'baz', 'foo', 'norf', 'qux'])
        self.assertEqual(nsw.language, 'bar')

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw += self.sw
        self.assertEqual(sorted(list(nsw)),
                         ['bar', 'baz', 'foo', 'norf', 'qux'])
        self.assertEqual(nsw.language, 'bar')

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw += ['tic', 'tac', 'toc']
        self.assertEqual(sorted(list(nsw)),
                         ['baz', 'norf', 'qux', 'tac', 'tic', 'toc'])

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw += 'tic'
        self.assertEqual(sorted(list(nsw)),
                         ['baz', 'norf', 'qux', 'tic'])

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw += unicode('tic')
        self.assertEqual(sorted(list(nsw)),
                         ['baz', 'norf', 'qux', 'tic'])

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        self.assertRaises(TypeError, nsw.__add__, object())
        self.assertEqual(sorted(list(nsw)),
                         ['baz', 'norf', 'qux'])

    def test_sub(self):
        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw = nsw - self.sw
        self.assertEqual(sorted(list(nsw)), ['norf', 'qux'])
        self.assertEqual(nsw.language, 'bar')

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw -= self.sw
        self.assertEqual(sorted(list(nsw)), ['norf', 'qux'])
        self.assertEqual(nsw.language, 'bar')

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw -= ['tic', 'tac', 'toc', 'qux']
        self.assertEqual(sorted(list(nsw)),
                         ['baz', 'norf'])

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw -= 'baz'
        self.assertEqual(sorted(list(nsw)),
                         ['norf', 'qux'])

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        nsw -= unicode('baz')
        self.assertEqual(sorted(list(nsw)),
                         ['norf', 'qux'])

        nsw = StopWord('bar', ['baz', 'qux', 'norf'])
        self.assertRaises(TypeError, nsw.__sub__, object())
        self.assertEqual(sorted(list(nsw)),
                         ['baz', 'norf', 'qux'])


class StopWordRebaseTestCase(TestCase):

    def check_stop_word_rebase(self, inpout, outpout, sept):
        sw = StopWord('test', sept)
        self.assertEqual(sw.rebase(inpout), outpout)

    def test_stopword_rebase_first(self):
        """
        Test with first word in text
        """
        self.check_stop_word_rebase(
            'Comme je viens de te le dire',
            'je viens de te le dire',
            ['comme'])

    def test_stopword_rebase_middle(self):
        """
        Test with word in middle of text
        """
        self.check_stop_word_rebase(
            'Comme je viens de te le dire',
            'Comme je de te le dire',
            ['viens'])

    def test_stopword_rebase_newline(self):
        """
        Test with newline between two words
        """
        self.check_stop_word_rebase(
            'Comme je\nviens de te le dire',
            'Comme\nde te le dire',
            ['viens', 'je'])
        self.check_stop_word_rebase(
            'Comme je\nviens de te le dire',
            'Comme\nviens de te le dire',
            ['je'])
        self.check_stop_word_rebase(
            'Comme je\nviens de te le dire',
            'Comme je\nde te le dire',
            ['viens'])

    def test_stopword_rebase_two_escape_code(self):
        """
        Test with newline and tab before word
        """
        self.check_stop_word_rebase(
            'Comme je\n\tviens de te le dire',
            'Comme je\n\tde te le dire',
            ['viens'])
        self.check_stop_word_rebase(
            'Comme je viens\n\tde te le dire',
            'Comme je\n\tde te le dire',
            ['viens'])

    def test_stopword_dont_rebase(self):
        """
        Test with newline before word
        """
        self.check_stop_word_rebase(
            'Comme je viensbhgfds de te le dire',
            'Comme je viensbhgfds de te le dire',
            ['viens'])
