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
        if x and y:
            self.canvas = self.build_canvas(x, y)

    def build_canvas(self, x, y):

        if not x >= 0 or not y >= 0:
            raise ValueError('canvas size must be positive')

        self.canvas = [['O' for i in range(x)] for i in range(y)]

    def picture(self):
        import pdb; pdb.set_trace()
        return self.canvas
