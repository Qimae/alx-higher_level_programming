#!/usr/bin/python3
"""
Module square

Defines class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Methods:
        __init__(self, size, x=0, y=0, id=None)
        __str__(self)
        size(self)
        size(self, value)
        update(self, *args, **kwargs)
        to_dictionary(self)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """ return [Square] (<id>) <x>/<y> - <size>"""
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                else:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            else:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        dictionary = {}

        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
