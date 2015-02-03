"""
Mots-vides
"""
from mots_vides.stop_words import StopWord
from mots_vides.factory import StopWordFactory

__all__ = ['StopWord', 'StopWordFactory',
           'default_factory', 'stop_words']

default_factory = StopWordFactory()

def stop_words(language, fail_safe=True):
    """
    Shortcut for getting stop words
    without initializing a factory.
    """
    return default_factory.get_stop_words(
        language, fail_safe=fail_safe)
