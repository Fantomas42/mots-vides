"""
Merger command line script for building collections of stop words
"""
import sys
from argparse import ArgumentParser


def cmdline(argv=sys.argv[1:]):
    parser = ArgumentParser(
        description='Create and merge collections of stop words')
    parser.add_argument(
        'language', help='The language used in the collection')
    parser.add_argument('sources', metavar='FILE', nargs='+',
                        help='Source files to parse')
    options = parser.parse_args(argv)
    import pdb; pdb.set_trace()
