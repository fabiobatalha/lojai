# coding: utf-8
import unittest

from paint.canvas import Canvas


class TestCode(unittest.TestCase):

    def test_instanciating_canvas(self):
        """
        Testing instanciating the class canvas.
        """

        canvas = Canvas(3, 3)

        expected = [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
            ['O', 'O', 'O']
        ]

        self.assertEqual(expected, canvas.picture())
