# coding: utf-8


class Canvas(object):

    def __init__(self, x=None, y=None):
        """
        This class build a painting matrix with the x and y arguments, where
        x is the horizontal size and y is the vertical size.

        Arguments:
        x -- horizontal size
        y -- vertical size
        """
        self.canvas = None

        if x and y:
            self.build_canvas(x, y)

    def build_canvas(self, x, y):

        x = int(x)
        y = int(y)

        if not x >= 0 or not y >= 0:
            raise ValueError('canvas size must be positive')

        self.canvas = [['O' for i in range(y)] for i in range(x)]

    def print_pixel(self, x, y, color):
        """
        This method parses the args of the command L of the enunciation

        Attributes:
        x -- integer
        y -- integer
        color -- any valid string or interger
        """
        x = int(x)-1
        y = int(y)-1

        if not x > 0 and not y > 0:
            raise ValueError('x and y must be positive intergers')

        self.canvas[x][y] = color


    def print_vertical(self, x, y1, y2, color):
        """
        This method parses the args of the command V of the enunciation

        Attributes:
        x -- integer (column index)
        y1 -- integer (vertical start point)
        y2 -- integer (vertical end point)
        color -- any valid string or interger
        """
        x = int(x)-1
        y1 = int(y1)-1
        y2 = int(y2)-1

        if not x >= 0 and not y1 >= 0 and not y2 >= 0:
            raise ValueError('x, y1 and y2 must be positive intergers')

        if not y2 >= y1:
            raise ValueError('y2 must be greather than y1')

        for y in range(y1, y2+1):
            self.canvas[x][y] = color

    def print_horizontal(self, y, x1, x2, color):
        """
        This method parses the args of the command H of the enunciation

        Attributes:
        y -- integer (line index)
        x1 -- integer (horizontal start point)
        x2 -- integer (horizontal start point)
        color -- any valid string or interger
        """
        
        y = int(y)-1
        x1 = int(x1)-1
        x2 = int(x2)-1

        if not y > 0 and not x1 > 0 and not x2 > 0:
            raise ValueError('y, x1 and x2 must be positive intergers')

        if not x2 >= x1:
            raise ValueError('x2 must be greather than x1')

        for x in range(x1, x2+1):
            self.canvas[x][y] = color

    def print_region(self, x, y, color):
        """
        This method parses the args of the command F of the enunciation

        Attributes:
        x -- integer
        y -- integer
        color -- any valid string or interger
        """
        x = int(x)
        y = int(y)

        if not x > 0 and not y > 0:
            raise ValueError('x and y must be positive intergers')

        pass

    def print_square(self, x1, y1, x2, y2, color):
        """
        This method parses the args of the command K of the enunciation

        Attributes:
        y -- integer (line index)
        x1 -- integer (horizontal start point)
        y1 -- integer (horizontal start point)
        x2 -- integer (horizontal start point)
        y2 -- integer (horizontal start point)
        color -- any valid string or interger
        """
        
        x1 = int(x1)-1
        y1 = int(y1)-1
        x2 = int(x2)-1
        y2 = int(y2)-1

        if not y1 > 0 and not y2 > 0 and not x1 > 0 and not x2 > 0:
            raise ValueError('y1, y2, x1 and x2 must be positive intergers')

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                self.canvas[x][y] = color

    def write_file(self, filename):
        """
        This method parses the args of the command S of the enunciation
        """

        if len(filename) == 0:
            raise ValueError('file names must be informed')

        with open(filename,  'w') as f:
            f.write(self.picture)

    @property
    def picture(self):

        return '\r\n'.join(
            ['\t'.join([str(x) for x in i]) for i in zip(*self.canvas)]
        )
