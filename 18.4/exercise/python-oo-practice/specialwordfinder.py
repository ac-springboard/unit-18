from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """
    Extension of the WordFinder class to eliminate empty lines and comment lines

    >>> p = "/home/acampos/my/courses/spb/unit-18/18.4/exercise/python-oo-practice/words.txt"
    >>> swf = SpecialWordFinder(p)
    235896 words read

    >>> print(len(swf.words))
    7

    >>> wset = set(swf.words_original)
    >>> wsset = set(swf.words)
    >>> print(sorted(wset.intersection(wsset)))
    ['Zyzomys', 'Zyzzogeton', 'apple', 'kale', 'mango', 'parsnips', 'zythum']

    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.words_original = self.words  # For testing purposes, only.
        self.words = [word for word in self.words if word and not word.isspace() and not word.startswith('#')]
