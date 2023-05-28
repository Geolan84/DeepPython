"""unittest tests for CustomList class."""
import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    """TestCase for CustomList class."""
    def test_add_returned_type(self):
        """Tests type of returned result from addition."""
        self.assertIsInstance(CustomList([1, 2, 3])+[4, 8], CustomList)
        self.assertIsInstance([4, 8]+CustomList([1, 2, 3]), CustomList)
        self.assertIsInstance(CustomList(
            [4, 8])+CustomList([1, 2, 3]), CustomList)

    def test_sub_returned_type(self):
        """Tests type of returned result from subtraction."""
        self.assertIsInstance(CustomList([1, 2, 3])-[4, 8], CustomList)
        self.assertIsInstance([4, 8]-CustomList([1, 2, 3]), CustomList)
        self.assertIsInstance(CustomList(
            [4, 8])-CustomList([1, 2, 3]), CustomList)

    def test_str(self):
        """Tests string representation for CustomList instances."""
        # First check.
        custom_list = CustomList()
        self.assertEqual(str(custom_list), "Items: []; Sum: 0")
        self.assertEqual(list(custom_list), list(CustomList()))
        # Second check.
        custom_list = CustomList([1, 3, -5])
        self.assertEqual(
            str(custom_list), "Items: [1, 3, -5]; Sum: -1")
        self.assertEqual(list(custom_list), list(CustomList([1, 3, -5])))
        # Third check.
        custom_list = CustomList([-1, -4, 3, 2])
        self.assertEqual(
            str(custom_list), "Items: [-1, -4, 3, 2]; Sum: 0")
        self.assertEqual(list(custom_list), list(CustomList([-1, -4, 3, 2])))

    def test_lt(self):
        """Tests 'low than' comparison of CustomList instances."""
        # First check.
        left = CustomList([45, 92, 178, 23])
        right = CustomList([1000])
        self.assertTrue(left < right)
        self.assertEqual(list(left), list(CustomList([45, 92, 178, 23])))
        self.assertEqual(list(right), list(CustomList([1000])))
        # Second check.
        left = CustomList([500, 500])
        right = CustomList([45, 92, 178, 23])
        self.assertFalse(left < right)
        self.assertEqual(list(left), list(CustomList([500, 500])))
        self.assertEqual(list(right), list(CustomList([45, 92, 178, 23])))
        # Third check.
        left = CustomList([500])
        right = CustomList([100, 150, 250])
        self.assertFalse(left < right)
        self.assertEqual(list(left), list(CustomList([500])))
        self.assertEqual(list(right), list(CustomList([100, 150, 250])))

    def test_le(self):
        """Tests 'low than or equal to' comparison of CustomList instances."""
        # First check.
        left = CustomList([45, 92, 178, 23])
        right = CustomList([1000])
        self.assertTrue(left <= right)
        self.assertEqual(list(left), list(CustomList([45, 92, 178, 23])))
        self.assertEqual(list(right), list(CustomList([1000])))
        # Second check.
        left = CustomList([500, 500])
        right = CustomList([45, 92, 178, 23])
        self.assertFalse(left <= right)
        self.assertEqual(list(left), list(CustomList([500, 500])))
        self.assertEqual(list(right), list(CustomList([45, 92, 178, 23])))
        # Third check.
        left = CustomList([500])
        right = CustomList([100, 150, 250])
        self.assertTrue(left <= right)
        self.assertEqual(list(left), list(CustomList([500])))
        self.assertEqual(list(right), list(CustomList([100, 150, 250])))

    def test_eq(self):
        """Tests 'equal to' comparison of CustomList instances."""
        # First check. Fully equal by elements.
        left = CustomList([45, 92, 178, 22])
        right = CustomList([45, 92, 178, 22])
        self.assertTrue(left == right)
        self.assertEqual(list(left), list(CustomList([45, 92, 178, 22])))
        self.assertEqual(list(right), list(CustomList([45, 92, 178, 22])))
        # Second check. The same length, different numbers.
        right = CustomList([45, 92, 177, 23])
        self.assertTrue(left == right)
        self.assertEqual(list(left), list(CustomList([45, 92, 178, 22])))
        self.assertEqual(list(right), list(CustomList([45, 92, 177, 23])))
        # Third check. Different elements, numbers, but equal sums.
        left = CustomList([68, 92, 178])
        right = CustomList([45, 92, 178, 23])
        self.assertTrue(left == right)
        self.assertEqual(list(left), list(CustomList([68, 92, 178])))
        self.assertEqual(list(right), list(CustomList([45, 92, 178, 23])))
        # Fourth check. Symmetrical check of previous test.
        left = CustomList([45, 92, 178, 23])
        right = CustomList([68, 92, 178])
        self.assertTrue(left == right)
        self.assertEqual(list(right), list(CustomList([68, 92, 178])))
        self.assertEqual(list(left), list(CustomList([45, 92, 178, 23])))
        # Fifth check. Don't equal.
        left = CustomList([1, 45, 6])
        right = CustomList([1, 46, 6])
        self.assertFalse(left == right)
        self.assertEqual(list(left), list(CustomList([1, 45, 6])))
        self.assertEqual(list(right), list(CustomList([1, 46, 6])))

    def test_ne(self):
        """Tests 'not equal to' comparison of CustomList instances."""
        # First check.
        left = CustomList([1, 2, 3])
        right = CustomList([1, 2, 3])
        self.assertFalse(left != right)
        self.assertEqual(list(left), list(CustomList([1, 2, 3])))
        self.assertEqual(list(right), list(CustomList([1, 2, 3])))
        # Second check.
        right = CustomList([5, 1])
        self.assertFalse(left != right)
        self.assertEqual(list(left), list(CustomList([1, 2, 3])))
        self.assertEqual(list(right), list(CustomList([5, 1])))
        # Third check.
        right = CustomList([2, 30])
        self.assertTrue(left != right)
        self.assertEqual(list(left), list(CustomList([1, 2, 3])))
        self.assertEqual(list(right), list(CustomList([2, 30])))

    def test_gt(self):
        """Tests 'greater than' comparison of CustomList instances."""
        # First check. The same length, different sums.
        left = CustomList([1, 2, 4])
        right = CustomList([1, 2, 3])
        self.assertTrue(left > right)
        self.assertEqual(list(left), list(CustomList([1, 2, 4])))
        self.assertEqual(list(right), list(CustomList([1, 2, 3])))
        # Second check. Equal elements.
        left = CustomList([1, 2, 3])
        self.assertFalse(left > right)
        self.assertEqual(list(left), list(CustomList([1, 2, 3])))
        self.assertEqual(list(right), list(CustomList([1, 2, 3])))
        # Third check. Different lengths, not equal sums.
        left = CustomList([1, 2])
        self.assertFalse(left > right)
        self.assertEqual(list(left), list(CustomList([1, 2])))
        self.assertEqual(list(right), list(CustomList([1, 2, 3])))

    def test_ge(self):
        """Tests 'low than or equal to' comparison of CustomList instances."""
        # First check.
        left = CustomList([1, 2, 4])
        right = CustomList([1, 2, 3])
        self.assertTrue(left >= right)
        self.assertEqual(list(left), list(CustomList([1, 2, 4])))
        self.assertEqual(list(right), list(CustomList([1, 2, 3])))
        # Second check.
        left = CustomList([1, 2, 3])
        self.assertTrue(left >= right)
        self.assertEqual(list(left), list(CustomList([1, 2, 3])))
        self.assertEqual(list(right), list(CustomList([1, 2, 3])))
        # Third check.
        left = CustomList([1, 2])
        self.assertFalse(left >= right)
        self.assertEqual(list(left), list(CustomList([1, 2])))
        self.assertEqual(list(right), list(CustomList([1, 2, 3])))

    def test_addition_dif_types(self):
        """Tests correctness of different types addition."""
        # First check.
        left = CustomList([23, 41, 96])
        right = [92, 4]
        self.assertEqual(list(left + right), list(CustomList([115, 45, 96])))
        self.assertEqual(list(left), list(CustomList([23, 41, 96])))
        self.assertEqual(right, [92, 4])
        # Second check.
        left = CustomList([100, -40, 96])
        right = [92, 4, 6, 10]
        self.assertEqual(list(left + right),
                         list(CustomList([192, -36, 102, 10])))
        self.assertEqual(list(left), list(CustomList([100, -40, 96])))
        self.assertEqual(right, [92, 4, 6, 10])
        # Third check.
        left = [92, 4]
        right = CustomList([23, 41, 96])
        self.assertEqual(list(left + right), list(CustomList([115, 45, 96])))
        self.assertEqual(left, [92, 4])
        self.assertEqual(list(right), list(CustomList([23, 41, 96])))
        # Fourth check.
        left = [92, 4, 150, -43]
        right = CustomList([3, 37, -10])
        self.assertEqual(list(left + right),
                         list(CustomList([95, 41, 140, -43])))
        self.assertEqual(left, [92, 4, 150, -43])
        self.assertEqual(list(right), list(CustomList([3, 37, -10])))

    def test_subtraction_dif_types(self):
        """Tests correctness of different types subtraction."""
        # First check.
        left = CustomList([23, 41, 96])
        right = [92, 4]
        self.assertEqual(list(left - right), list(CustomList([-69, 37, 96])))
        self.assertEqual(list(left), list(CustomList([23, 41, 96])))
        self.assertEqual(right, [92, 4])
        # Second check.
        left = CustomList([100, -40, 96])
        right = [92, 4, 6, 10]
        self.assertEqual(list(left - right),
                         list(CustomList([8, -44, 90, -10])))
        self.assertEqual(list(left), list(CustomList([100, -40, 96])))
        self.assertEqual(right, [92, 4, 6, 10])
        # Third check.
        left = [92, 4]
        right = CustomList([23, 41, 96])
        self.assertEqual(list(left - right), list(CustomList([69, -37, -96])))
        self.assertEqual(left, [92, 4])
        self.assertEqual(list(right), list(CustomList([23, 41, 96])))
        # Fourth check.
        left = [92, 4, 150, -43]
        right = CustomList([3, 37, -10])
        self.assertEqual(list(left - right),
                         list(CustomList([89, -33, 160, -43])))
        self.assertEqual(left, [92, 4, 150, -43])
        self.assertEqual(list(right), list(CustomList([3, 37, -10])))

    def test_addition(self):
        """Extra tests of addition's corectness."""
        # First check.
        left = CustomList([5, 1, 3, 7])
        right = CustomList([1, 2, 7])
        self.assertEqual(list(left+right), list(CustomList([6, 3, 10, 7])))
        self.assertEqual(list(left), list(CustomList([5, 1, 3, 7])))
        self.assertEqual(list(right), list(CustomList([1, 2, 7])))
        # Second check.
        left = CustomList([1])
        right = CustomList([2, 5])
        self.assertEqual(list(left+right), list(CustomList([3, 5])))
        self.assertEqual(list(left), list(CustomList([1])))
        self.assertEqual(list(right), list(CustomList([2, 5])))

    def test_subtraction(self):
        """Extra tests of subtraction's corectness."""
        # First check.
        left = CustomList([5, 1, 3, 7])
        right = CustomList([1, 2, 7])
        self.assertEqual(list(left-right), list(CustomList([4, -1, -4, 7])))
        self.assertEqual(list(left), list(CustomList([5, 1, 3, 7])))
        self.assertEqual(list(right), list(CustomList([1, 2, 7])))
        # Second check.
        left = CustomList([1])
        right = CustomList([2, 5])
        self.assertEqual(list(left-right), list(CustomList([-1, -5])))
        self.assertEqual(list(left), list(CustomList([1])))
        self.assertEqual(list(right), list(CustomList([2, 5])))

    def test_add_incorrect_types(self):
        """Tests incompatibility of types in addition."""
        with self.assertRaises(AttributeError):
            CustomList([1, 2, 3])+"test"
        with self.assertRaises(AttributeError):
            CustomList([1, 2, 3])+5
        with self.assertRaises(AttributeError):
            CustomList([1, 2, 3])+{1, 2, 3}
        with self.assertRaises(AttributeError):
            CustomList([1, 2, 3])+{"a": "b"}
        with self.assertRaises(AttributeError):
            "test"+CustomList([1, 2, 3])
        with self.assertRaises(AttributeError):
            5+CustomList([1, 2, 3])
        with self.assertRaises(AttributeError):
            {1, 2, 3} + CustomList([1, 2, 3])
        with self.assertRaises(AttributeError):
            {"a": "b"} + CustomList([1, 2, 3])

    def test_sub_incorrect_types(self):
        """Tests incompatibility of types in subtraction."""
        with self.assertRaises(AttributeError):
            CustomList([1, 2, 3])-"test"
        with self.assertRaises(AttributeError):
            CustomList([1, 2, 3])-5
        with self.assertRaises(AttributeError):
            CustomList([1, 2, 3])-{1, 2, 3}
        with self.assertRaises(AttributeError):
            CustomList([1, 2, 3])-{"a": "b"}
        with self.assertRaises(AttributeError):
            "test"-CustomList([1, 2, 3])
        with self.assertRaises(AttributeError):
            5-CustomList([1, 2, 3])
        with self.assertRaises(AttributeError):
            {1, 2, 3} - CustomList([1, 2, 3])
        with self.assertRaises(AttributeError):
            {"a": "b"} - CustomList([1, 2, 3])
