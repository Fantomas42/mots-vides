"""
StopWord Python container, managing collection of stop words.
"""
import re


class StopWord(object):

    def __init__(self, language, collection=[]):
        """
        Initializes Stopword with a given language
        and collection empty or not.
        """
        self.language = language
        self.collection = set(collection)
        self.regex = None

    def __add__(self, entry):
        """
        Add an entry or collection to an instance
        """
        if isinstance(entry, str):
            self.collection.add(entry)
        else:
            self.collection = self.collection.union(entry)

        return self

    def __sub__(self, entry):
        """
        Substract an entry or collection to an instance
        """
        if isinstance(entry, str):
            self.collection.remove(entry)
        else:
            self.collection = self.collection.difference(entry)

        return self

    def __len__(self):
        """
        Return the collection lenght
        """
        return len(self.collection)

    def __contains__(self, elem):
        """
        self.__contains__(elem) <==> elem in self.collection
        """
        return self.collection.__contains__(elem)

    def __iter__(self):
        """
        self.__iter__() <==> iter(self.collection)
        """
        return self.collection.__iter__()

    def _compile_regex(self, word):
        self.regex = re.compile(r'((^| ){0}(| ))|({0} )|{0}'.format(word), flags=re.IGNORECASE)
        return self.regex

    def rebase(self, text):
        for word in self.collection:
            current_regex = self._compile_regex(word)
            text = current_regex.sub('', text).strip()
        return text
