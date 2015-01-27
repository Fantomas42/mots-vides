import os
import codecs
from constants import DATA_DIRECTORY

DATA_DIRECTORY = DATA_DIRECTORY

LOADED_LANGUAGES = {}


class StopWordFactory(object):

    def __init__(self, path=DATA_DIRECTORY):
        self.path = path

    def get_stop_words(self, language, fail_safe=False):
        if not LOADED_LANGUAGES.get(language, False):
            try:
                language_file = codecs.open(
                    '{0}{1}.txt'.format(self.path, language),
                    'r',
                    encoding='utf-8-sig'
                )
                collection = set(language_file.read().splitlines())
            except:
                if not fail_safe:
                    raise Exception("No file here!!!!!!!")
                collection = set()

            stop_words = StopWord(
                language,
                collection
            )

            LOADED_LANGUAGES[language] = stop_words
            return stop_words

        return LOADED_LANGUAGES[language]

    def get_collection_filename(self, language):
        if os.path.exists('{0}{1}.txt'.format(self.path, language)):
            return '{0}.txt'.format(language)
        else:
            raise Exception("No file here!!!!!!!")

    def get_available_language(cls):
        return os.listdir(self.path)

    def write_collection(self, filename, collection):
        language_file = codecs.open(
            '{0}{1}'.format(self.path, filename),
            'w+',
            encoding='utf8'
            )
        for item in collection:
            language_file.write("{0}\n".format(item.encode('utf-8')))


class StopWord(object):

    def __init__(self, language, collection=None):
        self.language = language
        self.collection = collection

    def __add__(self, entry):
        if isinstance(entry, str):
            self.collection.add(entry)
        else:
            self.collection = self.collection.union(entry)

    def __sub__(self, entry):
        if isinstance(entry, str):
            self.collection.remove(entry)
        else:
            self.collection = self.collection.difference(entry)

    def __len__(self):
        return len(self.collection)

    def __contains__(self, elem):
        return self.collection.__contains__(elem)

    def __iter__(self):
        return self.collection.__iter__()
