from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """
    Extension of the WordFinder class to eliminate empty lines and comment lines

    >>> p = "/home/acampos/my/courses/spb/unit-18/18.4/exercise/python-oo-practice/words.txt"
    >>> swf = SpecialWordFinder(p)
    235896 words read

    >>> len(swf.words) == 235896
    True

    >>> wset = set(swf.words)
    >>> wsset = set(swf.words_special)
    >>> print(wset.difference(wsset))
    {'', '# Veggies', '# Fruits'}

    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.words = [word for word in self.words if word and not word.isspace() and not word.startswith('#')]
