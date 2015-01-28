"""
Tests for StopWordFactory
"""
import os
from tempfile import NamedTemporaryFile

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

    def test_get_stopwords_cache(self):
        pass

    def test_get_stopwords_shortcuts(self):
        pass

    def test_get_stopwords_fail_safe(self):
        pass

    def test_available_languages(self):
        self.assertEqual(self.factory.available_languages,
                         ['klingon', 'sindarin'])
        self.factory.data_directory = '/brutal/change/'
        self.assertEqual(self.factory.available_languages,
                         ['klingon', 'sindarin'])

    def test_get_collection_filename(self):
        filename = self.factory.get_collection_filename('foo')
        self.assertTrue(filename.endswith('foo.txt'))
        self.assertTrue(filename.startswith(self.data_directory))

    def test_read_collection(self):
        collection_file = NamedTemporaryFile()
        collection_text = 'egor\n\n   \nai\n'
        collection_file.write('\xef\xbb\xbf')  # BOM
        collection_file.write(collection_text.encode('utf-8'))
        collection_file.seek(0)
        collection = self.factory.read_collection(collection_file.name)
        self.assertEqual(collection, ['egor', 'ai'])
        collection_file.close()

    def test_write_collection(self):
        collection_file = NamedTemporaryFile()
        self.factory.write_collection(
            collection_file.name,
            ['nuq', "HIja'", "ghobe'", 'naDev'])
        collection_file.seek(0)
        self.assertEqual(collection_file.read(),
                         "HIja'\nghobe'\nnaDev\nnuq")
        collection_file.close()
