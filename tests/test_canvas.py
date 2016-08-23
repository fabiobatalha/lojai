# coding: utf-8
import unittest

from paint.canvas import Canvas


class TestCanvas(unittest.TestCase):

    def setUp(self):

        self.canvas = Canvas(3, 3)

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

        self.assertEqual(expected, canvas.canvas)

    def test_pixels_around(self):

        canvas = Canvas(4, 4)

        pixels_around = canvas.pixels_around(2, 3)

        expected = [
            (1, 2), (2, 2), (3, 2), (1, 3), (3, 3), (1, 4), (2, 4), (3, 4)
        ]

        self.assertEqual(expected, pixels_around)

    def test_build_canvas_1(self):
        """
        Testing create matrix command with invalid args signature
        expecting: x, y
        receiving: x

        raise TypeError
        """

        with self.assertRaises(TypeError):
            self.canvas.build_canvas(1)

    def test_build_canvas_2(self):
        """
        Testing create matrix command with invalid args signature
        expecting: x, y
        receiving: x, y, c

        raise TypeError
        """

        with self.assertRaises(TypeError):
            self.canvas.build_canvas(1, 2, 'C')

    def test_build_canvas_3(self):
        """
        Testing create matrix command with valid signature
        expecting: x, y
        receiving: x, y
        """
        self.canvas.build_canvas(2, 4)

        expected = [['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O']]

        self.assertTrue(expected, self.canvas.canvas)

    def test_build_canvas_4(self):
        """
        Testing create matrix command with valid signature but invalid
        parameteres

        expecting: x and y must be positive intergers
        receiving: 0, -1

        raise ValueError
        """
        with self.assertRaises(ValueError):
            self.canvas.build_canvas(0, -1)

    def test_build_canvas_5(self):
        """
        Testing create matrix command with invalid signature

        expecting: x and y must be positive intergers
        receiving: a, b

        raise ValueError
        """
        with self.assertRaises(ValueError):
            self.canvas.build_canvas('a', 'b')

    def test_build_canvas_6(self):
        """
        Testing printing pixel command with valid signature

        expecting: x and y must be positive intergers, and c
        receiving: '1', '2', 'C'
        """
        self.canvas.print_pixel('1', '2', 'C')

        expected = [['O', 'C', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]

        self.assertTrue(expected, self.canvas.canvas)

    def test_build_canvas_7(self):
        """
        Testing create matrix command with valid signature

        expecting: x and y must be positive intergers
        receiving: '1', '2'
        """

        self.canvas.build_canvas('1', '2')

        expected = [['O', 'O']]

        self.assertEqual(expected, self.canvas.canvas)

    def test_print_pixel_1(self):
        """
        Testing printing pixel command with invalid args signature
        expecting: x, y, c
        receiving: x

        raise TypeError
        """

        with self.assertRaises(TypeError):
            self.canvas.print_pixel(1)

    def test_print_pixel_2(self):
        """
        Testing printing pixel command with invalid args signature
        expecting: x, y, c
        receiving: x, y, c, d

        raise TypeError
        """

        with self.assertRaises(TypeError):
            self.canvas.print_pixel(1, 2, 'C', 'D')

    def test_print_pixel_3(self):
        """
        Testing printing pixel command with valid signature
        expecting: x, y, c
        receiving: x, y, c
        """

        self.canvas.print_pixel(2, 3, 'C')

        expected = [['O', 'O', 'O'], ['O', 'O', 'C'], ['O', 'O', 'O']]

        self.assertTrue(expected, self.canvas.canvas)

    def test_build_canvas_4(self):
        """
        Testing create matrix command with valid signature but invalid
        parameteres

        expecting: x and y must be positive intergers
        receiving: 0, -1

        raise ValueError
        """
        with self.assertRaises(ValueError):
            self.canvas.print_pixel(0, -1, 'C')

    def test_print_pixel_5(self):
        """
        Testing printing pixel command with invalid signature

        expecting: x and y must be positive intergers, and c
        receiving: a, b, c

        raise ValueError
        """
        with self.assertRaises(ValueError):
            self.canvas.print_pixel('a', 'b', 'c')

    def test_print_vertical_1(self):
        """
        Testing vertical print command with invalid args signature
        expecting: x, y1, y2, c
        receiving: x

        raise TypeError
        """

        with self.assertRaises(TypeError):
            self.canvas.print_vertical(1)

    def test_print_vertical_2(self):
        """
        Testing vertical print command with invalid args signature
        expecting: x, y1, y2, c
        receiving: x, y1, y2, c, d

        raise TypeError
        """

        with self.assertRaises(TypeError):
            self.canvas.print_vertical(1, 2, 3, 'C', 'D')

    def test_print_vertical_3(self):
        """
        Testing vertical print command with valid signature
        expecting: x, y1, y2, c
        receiving: x, y1, y2, c
        """

        self.canvas.print_vertical(2, 1, 3, 'C')

        expected = [['O', 'O', 'O'], ['C', 'C', 'C'], ['O', 'O', 'O']]

        self.assertEqual(expected, self.canvas.canvas)

    def test_print_vertical_4(self):
        """
        Testing vertical print command with valid signature but invalid
        parameteres

        expecting: x, y1, y2 must be positive intergers and C
        receiving: 0, 0, -1

        raise ValueError
        """
        with self.assertRaises(ValueError):
            self.canvas.print_vertical(0, 0, -1, 'C')

    def test_print_vertical_5(self):
        """
        Testing vertical print command with invalid signature

        expecting: x, y1, y2 must be positive intergers, and c
        receiving: a, b, c, d

        raise ValueError
        """
        with self.assertRaises(ValueError):
            self.canvas.print_vertical('a', 'b', 'c', 'd')

    def test_print_vertical_6(self):
        """
        Testing vertical print command with valid signature

        expecting: x, y1, y2 must be positive intergers, and c
        receiving: '1', '2', '3', 'C'
        """

        self.canvas.print_vertical('1', '2', '3', 'C')

        expected = [['O', 'C', 'C'], ['O', 'O', 'O'], ['O', 'O', 'O']]

        self.assertEqual(expected, self.canvas.canvas)

    def test_print_vertical_7(self):
        """
        Testing vertical print command with valid signature

        expecting: x, y1, y2 must be positive intergers, and c
        receiving: '1', '10', '3', 'C'

        raise ValueError('y2 must be greather then y1')
        """
        with self.assertRaises(ValueError):
            self.canvas.print_vertical('1', '10', '3', 'C')

    def test_print_horizontal_1(self):
        """
        Testing horizontal print command with invalid args signature
        expecting: y, x1, x2, c
        receiving: y

        raise TypeError
        """

        with self.assertRaises(TypeError):
            self.canvas.print_horizontal(1)

    def test_print_horizontal_2(self):
        """
        Testing horizontal print command with invalid args signature
        expecting: y, x1, x2, c
        receiving: y, x1, x2, c, d

        raise TypeError
        """

        with self.assertRaises(TypeError):
            self.canvas.print_horizontal(1, 2, 3, 'C', 'D')

    def test_print_horizontal_3(self):
        """
        Testing horizontal print command with valid signature
        expecting: y, x1, x2, c
        receiving: y, x1, x2, c
        """

        self.canvas.print_horizontal(2, 1, 3, 'C')

        expected = [['O', 'C', 'O'], ['O', 'C', 'O'], ['O', 'C', 'O']]

        self.assertEqual(expected, self.canvas.canvas)

    def test_print_horizontal_4(self):
        """
        Testing horizontal print command with valid signature but invalid
        parameteres

        expecting: y, x1, x2 must be positive intergers and C
        receiving: 0, 0, -1

        raise ValueError
        """
        with self.assertRaises(ValueError):
            self.canvas.print_horizontal(0, 0, -1, 'C')

    def test_print_horizontal_5(self):
        """
        Testing horizontal print command with invalid signature

        expecting: y, x1, x2 must be positive intergers, and c
        receiving: a, b, c, d

        raise ValueError
        """
        with self.assertRaises(ValueError):
            self.canvas.print_horizontal('a', 'b', 'c', 'd')

    def test_print_horizontal_6(self):
        """
        Testing horizontal print command with valid signature

        expecting: y, x1, x2 must be positive intergers, and c
        receiving: '1', '2', '3', 'C'

        return True
        """

        self.canvas.print_horizontal('1', '2', '3', 'C')

        expected = [['O', 'O', 'O'], ['C', 'O', 'O'], ['C', 'O', 'O']]

        self.assertEqual(expected, self.canvas.canvas)

    def test_print_horizontal_7(self):
        """
        Testing horizontal print command with valid signature

        expecting: y, x1, x2 must be positive intergers, and c
        receiving: '1', '10', '3', 'C'

        raise ValueError('y2 must be greather then y1')
        """
        with self.assertRaises(ValueError):
            self.canvas.print_horizontal('1', '10', '3', 'C')

    def test_print_square_1(self):
        """
        Testing square print command with valid signature

        expecting: x1, y1, x2, x2 must be positive intergers, and c
        receiving: '1', '2', '5', '1', 'C'
        """

        self.canvas.print_square('1', '1', '2', '3', 'C')

        expected = [['C', 'C', 'C'], ['C', 'C', 'C'], ['O', 'O', 'O']]

        self.assertEqual(expected, self.canvas.canvas)

    def test_print_square_2(self):
        """
        Testing square print command with invalid signature

        expecting: x1, y1, x2, x2 must be positive intergers, and c
        receiving: '1', '2', '1', 'C'
        """
        with self.assertRaises(TypeError):
            self.canvas.print_square('1', '2', '1', 'C')
