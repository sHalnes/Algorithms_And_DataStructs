import binary_search
import unittest

class KnownValues(unittest.TestCase):
    known_results = ((7, 6),# here first number - element to find, second number - position
                     (12, 11),
                     (80, 20),
                     (36, -1),
                     (91, -1),
                     (0, -1),
                     (1, 0),
                     )

    def test_to_known_values(self):
        list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 23, 24, 25, 26, 27, 28, 80, 89, 90]
        for element, position in self.known_results:
            #print('case: element {}, position {}'.format(element, position))
            result = binary_search.binary_search(list_values, element)
            self.assertEqual(position, result)


if __name__=='__main__':
    unittest.main()
