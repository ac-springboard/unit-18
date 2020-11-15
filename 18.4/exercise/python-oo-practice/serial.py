"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.default_start = start
        self.start = start
        """Generates incrementing serial numbers starting with any number (100 as default)
        """

    def generate(self):
        """Prints the next number in the series"""
        print(self.start)
        self.start += 1

    def reset(self):
        """Resets the starting number of the series to default"""
        self.start = self.default_start
