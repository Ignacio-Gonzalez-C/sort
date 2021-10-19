import unittest
import sort

class TestSortingAlgorithms(unittest.TestCase):

    def test_quick_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 4, 6, 1, 2, 0]
        sort.quick_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 4, 6])
        
    def test_quick_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [2, 4, 9, 2, 2, 7]
        sort.quick_sort(a)
        self.assertEqual(a, [2, 2, 2, 4, 7, 9])
        
    def test_quick_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1]
        sort.quick_sort(a)
        self.assertEqual(a, [1])

    def test_quick_sort_4(self):
        """
        Prueba caso general #3
        """
        a = [1, 0, 9, 0, 5, 9]
        sort.quick_sort(a)
        self.assertEqual(a, [0, 0, 1, 5, 9, 9])

    def test_insertion_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [2, 2, 0, 1, 4, 2]
        sort.inserion_sort(a)
        self.assertEqual(a, [0, 1, 2, 2, 2, 4])

    def test_insertion_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [9, 9, 9, 9, 0, 0]
        sort.inserion_sort(a)
        self.assertEqual(a, [0, 0, 9, 9, 9, 9])

    def test_insertion_sort_3(self):
        """
        Prueba caso general #3
        """
        a = [2, 8, 9, 4, 1, 50]
        sort.inserion_sort(a)
        self.assertEqual(a, [1, 2, 4, 8, 9, 50])
    
    def test_insertion_sort_4(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [5]
        sort.inserion_sort(a)
        self.assertEqual(a, [5])

    def test_bubble_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 0, 3, -5, 8, 3]
        sort.bubble_sort(a)
        self.assertEqual(a, [-5, 0, 1, 3, 3, 8])

    def test_bubble_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [1, 1, 1, 0, 2, -1]
        sort.bubble_sort(a)
        self.assertEqual(a, [-1, 0, 1, 1, 1, 2])

    def test_bubble_sort_3(self):
        """
        Prueba caso general #3
        """
        a = [-5, -10, 5, -1, 0, 1]
        sort.bubble_sort(a)
        self.assertEqual(a, [-10, -5, -1, 0, 1, 5])

    def test_bubble_sort_4(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [3]
        sort.bubble_sort(a)
        self.assertEqual(a, [3])

    def test_selection_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [9, 8, 7, 6, 4, 5]
        sort.selection_sort(a)
        self.assertEqual(a, [4, 5, 6, 7, 8, 9])

    def test_selection_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [0, 1, 0, 0, 0, -1]
        sort.selection_sort(a)
        self.assertEqual(a, [-1, 0, 0, 0, 0, 1])

    def test_selection_sort_3(self):
        """
        Prueba caso general #3
        """
        a = [-5, -8, 3, 80, -50]
        sort.selection_sort(a)
        self.assertEqual(a, [-50, -8, -5, 3, 80])

    def test_selection_sort_4(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [47]
        sort.selection_sort(a)
        self.assertEqual(a, [47])

if __name__ == '__main__':
    unittest.main()