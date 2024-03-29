#!/usr/bin/python3
"""
Module rectangle

Defines class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Attributes:
        __width
        __height
        __x
        __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        width(self)
        height(self)
        x(self)
        y(self)
        width(self, value)
        height(self, value)
        x(self, value)
        y(self, value)
        area(self)
        dispaly(self)
        __str__(self)
        update(self, *args, **kwargs)
        to_dictionary(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes width, height, x and y attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @property
    def height(self):
        """getter height"""
        return self.__height

    @property
    def x(self):
        """getter x"""
        return self.__x

    @property
    def y(self):
        """getter y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle with character #"""
        print("\n" * self.__y + "\n".join(" " * self.__x + "#" *
              self.__width for i in range(self.__height)))

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.__width = j
                elif i == 2:
                    self.__height = j
                elif i == 3:
                    self.__x = j
                else:
                    self.__y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""
        dictionary = {}

        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
