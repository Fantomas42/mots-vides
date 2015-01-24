"""
Merger command line script for building collections of stop words
"""
import os
import sys
from argparse import ArgumentParser

from mots_vides.constants import DATA_DIRECTORY
from mots_vides.stop_words import StopWord
from mots_vides.stop_words import StopWordFactory


def cmdline(argv=sys.argv[1:]):
    parser = ArgumentParser(
        description='Create and merge collections of stop words')
    parser.add_argument(
        'language', help='The language used in the collection')
    parser.add_argument('sources', metavar='FILE', nargs='+',
                        help='Source files to parse')
    options = parser.parse_args(argv)

    stop_words = StopWordFactory(
        fail_safe=True).get_stop_words(options.language)

    for source in options.sources:
        with open(source) as source_fd:
            collection = filter(str.strip, source_fd.readlines())
        stop_words += StopWord(options.language, collection)

    data_file = os.path.join(DATA_DIRECTORY, '%s.txt' % options.language)
    collection = stop_words.collection.sort()
    with open(data_file, 'w+') as data_fd:
        data_fd.truncate()
        data_fd.write('\n'.join(collection))
