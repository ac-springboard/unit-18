"""Word Finder: finds random words from a dictionary."""
from random import choice


class WordFinder:
    """This the WordFinder Class

    >>> p = "/home/acampos/my/courses/spb/unit-18/18.4/exercise/python-oo-practice/words.txt"
    >>> wf = WordFinder(p)
    235896 words read

    >>> wf.random() in wf.words
    True

    """

    def __init__(self, file_path):
        self.path = file_path
        self.words = None
        self.load_words(self.path)

    def load_words(self, path):
        """Loads the words in the provided path/file and prints the number of lines (words) loaded"""
        words_file = open(path, 'r')
        words_read = words_file.readlines()
        words_file.close()
        # self.words = [word.replace('\n', '') for word in words_read] # This works, too.
        self.words = [word[:-1:] for word in words_read]
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from the list of words in this instance"""
        return choice(self.words)

    def random(self, lst):
        """Returns a random word from the list of words from a given list
        Note: this method could be static.
        """
        return choice(lst)
