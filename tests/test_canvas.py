# coding: utf-8
import unittest

from paint.canvas import Canvas
from paint import commands

class TestCanvas(unittest.TestCase):

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

class TestCommands(unittest.TestCase):

    def test_parse_command_1(self):
        """
        Testing parsing command with empty line
        """
        with self.assertRaises(ValueError):
            commands.parse_command([])

    def test_parse_command_2(self):
        """
        Testing parsing command with unknow command
        """

        with self.assertRaises(ValueError):
            commands.parse_command(['M', '1', '2'])

    def test_parse_command_3(self):
        """
        Testing parsing command with invalid signature
        """

        with self.assertRaises(TypeError):
            commands.parse_command(['I', 1])

    def test_parse_create_matrix_1(self):
        """
        Testing parsing create matrix command with invalid args signature
        expecting: x, y
        receiving: x

        raise TypeError
        """

        with self.assertRaises(TypeError):
            commands.parse_create_matrix(1)

    def test_parse_create_matrix_2(self):
        """
        Testing parsing create matrix command with invalid args signature
        expecting: x, y
        receiving: x, y, c

        raise TypeError
        """

        with self.assertRaises(TypeError):
            commands.parse_create_matrix(1, 2, 'C')

    def test_parse_create_matrix_3(self):
        """
        Testing parsing create matrix command with valid signature
        expecting: x, y
        receiving: x, y

        return True
        """

        self.assertTrue(commands.parse_create_matrix(2, 4))

    def test_parse_create_matrix_4(self):
        """
        Testing parsing create matrix command with valid signature but invalid 
        parameteres

        expecting: x and y must be positive intergers
        receiving: 0, -1
        
        raise ValueError
        """
        with self.assertRaises(ValueError):
            commands.parse_create_matrix(0, -1)

    def test_parse_create_matrix_5(self):
        """
        Testing parsing create matrix command with invalid signature

        expecting: x and y must be positive intergers
        receiving: a, b

        raise ValueError
        """
        with self.assertRaises(ValueError):
            commands.parse_create_matrix('a', 'b')

    def test_parse_create_matrix_6(self):
        """
        Testing parsing create matrix command with valid signature

        expecting: x and y must be positive intergers
        receiving: '1', '2'

        return True
        """
        with self.assertRaises(ValueError):
            commands.parse_create_matrix('1', '2')

    def test_parse_print_pixel_1(self):
        """
        Testing parsing printing pixel command with invalid args signature
        expecting: x, y, c
        receiving: x

        raise TypeError
        """

        with self.assertRaises(TypeError):
            commands.parse_print_pixel(1)

    def test_parse_print_pixel_2(self):
        """
        Testing parsing printing pixel command with invalid args signature
        expecting: x, y, c
        receiving: x, y, c, d

        raise TypeError
        """

        with self.assertRaises(TypeError):
            commands.parse_print_pixel(1, 2, 'C', 'D')

    def test_parse_print_pixel_3(self):
        """
        Testing parsing printing pixel command with valid signature
        expecting: x, y, c
        receiving: x, y, c

        return True
        """

        self.assertTrue(commands.parse_print_pixel(2, 4, 'C'))

    def test_parse_create_matrix_4(self):
        """
        Testing parsing create matrix command with valid signature but invalid 
        parameteres

        expecting: x and y must be positive intergers
        receiving: 0, -1
        
        raise ValueError
        """
        with self.assertRaises(ValueError):
            commands.parse_print_pixel(0, -1, 'C')

    def test_parse_print_pixel_5(self):
        """
        Testing parsing printing pixel command with invalid signature

        expecting: x and y must be positive intergers, and c
        receiving: a, b, c

        raise ValueError
        """
        with self.assertRaises(ValueError):
            commands.parse_print_pixel('a', 'b', 'c')

    def test_parse_create_matrix_6(self):
        """
        Testing parsing printing pixel command with valid signature

        expecting: x and y must be positive intergers, and c
        receiving: '1', '2', 'C'

        return True
        """

        self.assertTrue(commands.parse_print_pixel('1', '2', 'C'))

    def test_parse_vertical_print_1(self):
        """
        Testing parsing vertical print command with invalid args signature
        expecting: x, y1, y2, c
        receiving: x

        raise TypeError
        """

        with self.assertRaises(TypeError):
            commands.parse_vertical_print(1)

    def test_parse_vertical_print_2(self):
        """
        Testing parsing vertical print command with invalid args signature
        expecting: x, y1, y2, c
        receiving: x, y1, y2, c, d

        raise TypeError
        """

        with self.assertRaises(TypeError):
            commands.parse_vertical_print(1, 2, 3, 'C', 'D')

    def test_parse_vertical_print_3(self):
        """
        Testing parsing vertical print command with valid signature
        expecting: x, y1, y2, c
        receiving: x, y1, y2, c

        return True
        """

        self.assertTrue(commands.parse_vertical_print(2, 4, 5, 'C'))

    def test_parse_vertical_print_4(self):
        """
        Testing parsing vertical print command with valid signature but invalid 
        parameteres

        expecting: x, y1, y2 must be positive intergers and C
        receiving: 0, 0, -1
        
        raise ValueError
        """
        with self.assertRaises(ValueError):
            commands.parse_vertical_print(0, 0, -1, 'C')

    def test_parse_vertical_print_5(self):
        """
        Testing parsing vertical print command with invalid signature

        expecting: x, y1, y2 must be positive intergers, and c
        receiving: a, b, c, d

        raise ValueError
        """
        with self.assertRaises(ValueError):
            commands.parse_vertical_print('a', 'b', 'c', 'd')

    def test_parse_vertical_print_6(self):
        """
        Testing parsing vertical print command with valid signature

        expecting: x, y1, y2 must be positive intergers, and c
        receiving: '1', '2', '3', 'C'

        return True
        """

        self.assertTrue(commands.parse_vertical_print('1', '2', '3', 'C'))

    def test_parse_vertical_print_7(self):
        """
        Testing parsing vertical print command with valid signature

        expecting: x, y1, y2 must be positive intergers, and c
        receiving: '1', '10', '3', 'C'

        raise ValueError('y2 must be greather then y1')
        """
        with self.assertRaises(ValueError):
            commands.parse_vertical_print('1', '10', '3', 'C')

    def test_parse_horizontal_print_1(self):
        """
        Testing parsing horizontal print command with invalid args signature
        expecting: y, x1, x2, c
        receiving: y

        raise TypeError
        """

        with self.assertRaises(TypeError):
            commands.parse_horizontal_print(1)

    def test_parse_horizontal_print_2(self):
        """
        Testing parsing horizontal print command with invalid args signature
        expecting: y, x1, x2, c
        receiving: y, x1, x2, c, d

        raise TypeError
        """

        with self.assertRaises(TypeError):
            commands.parse_horizontal_print(1, 2, 3, 'C', 'D')

    def test_parse_horizontal_print_3(self):
        """
        Testing parsing horizontal print command with valid signature
        expecting: y, x1, x2, c
        receiving: y, x1, x2, c

        return True
        """

        self.assertTrue(commands.parse_horizontal_print(2, 4, 5, 'C'))

    def test_parse_horizontal_print_4(self):
        """
        Testing parsing horizontal print command with valid signature but invalid 
        parameteres

        expecting: y, x1, x2 must be positive intergers and C
        receiving: 0, 0, -1
        
        raise ValueError
        """
        with self.assertRaises(ValueError):
            commands.parse_horizontal_print(0, 0, -1, 'C')

    def test_parse_horizontal_print_5(self):
        """
        Testing parsing horizontal print command with invalid signature

        expecting: y, x1, x2 must be positive intergers, and c
        receiving: a, b, c, d

        raise ValueError
        """
        with self.assertRaises(ValueError):
            commands.parse_horizontal_print('a', 'b', 'c', 'd')

    def test_parse_horizontal_print_6(self):
        """
        Testing parsing horizontal print command with valid signature

        expecting: y, x1, x2 must be positive intergers, and c
        receiving: '1', '2', '3', 'C'

        return True
        """

        self.assertTrue(commands.parse_horizontal_print('1', '2', '3', 'C'))

    def test_parse_horizontal_print_7(self):
        """
        Testing parsing horizontal print command with valid signature

        expecting: y, x1, x2 must be positive intergers, and c
        receiving: '1', '10', '3', 'C'

        raise ValueError('y2 must be greather then y1')
        """
        with self.assertRaises(ValueError):
            commands.parse_horizontal_print('1', '10', '3', 'C')

    def test_parse_square_print_1(self):
        """
        Testing parsing square print command with valid signature

        expecting: x1, y1, x2, x2 must be positive intergers, and c
        receiving: '1', '2', '5', '1', 'C'

        """

        commands.parse_square_print('1', '2', '5', '1', 'C')

    def test_parse_square_print_2(self):
        """
        Testing parsing square print command with invalid signature

        expecting: x1, y1, x2, x2 must be positive intergers, and c
        receiving: '1', '2',  '1', 'C'

        """
        with self.assertRaises(TypeError):
            commands.parse_square_print('1', '2', '1', 'C')
