"""
StopWord Python container, managing collection of stop words.
"""


class StopWord(object):

    def __init__(self, language, collection=[]):
        self.language = language
        self.collection = set(collection)

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
