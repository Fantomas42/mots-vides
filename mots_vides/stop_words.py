"""
StopWord Python container, managing collection of stop words.
"""
import re

TEXT_TYPE_LIST = ('str', 'unicode', 'byte')


class StopWord(object):
    """
    Object managing collection of stop words for a given language.
    """

    def __init__(self, language, collection=[]):
        """
        Initializes with a given language and an optional collection.
        """
        self.language = language
        self.collection = set(collection)

    def __add__(self, entry):
        """
        Adds an entry or collection of entries to an instance.
        """
        if type(entry).__name__ in TEXT_TYPE_LIST:
            self.collection.add(entry)
        else:
            self.collection = self.collection.union(entry)

        return self

    def __sub__(self, entry):
        """
        Substracts an entry or collection of entries to an instance.
        """
        if type(entry).__name__ in TEXT_TYPE_LIST:
            self.collection.remove(entry)
        else:
            self.collection = self.collection.difference(entry)

        return self

    def __len__(self):
        """
        Returns the collection length.
        """
        return self.collection.__len__()

    def __contains__(self, entry):
        """
        Checks if an entry is in collection.
        """
        return self.collection.__contains__(entry)

    def __iter__(self):
        """
        Iterates over the collection.
        """
        return self.collection.__iter__()

    def _compile_regex(self, word):
        return re.compile(
            r'((^| ){0})|({0} )|{0}'.format('((?<!\w)'+word+'(?!\w))'),
            flags=re.IGNORECASE
        )

    def rebase(self, text):
        for word in self.collection:
            current_regex = self._compile_regex(word)
            text = current_regex.sub('', text).strip()
        return text
