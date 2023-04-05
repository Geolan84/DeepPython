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
        self.assertEqual(str(CustomList()), "Items: []; Sum: 0")
        self.assertEqual(
            str(CustomList([1, 3, -5])), "Items: [1, 3, -5]; Sum: -1")
        self.assertEqual(
            str(CustomList([-1, -4, 3, 2])), "Items: [-1, -4, 3, 2]; Sum: 0")

    def test_lt(self):
        """Tests 'low than' comparison of CustomList instances."""
        self.assertTrue(CustomList([45, 92, 178, 23]) < CustomList([1000]))
        self.assertFalse(CustomList([500, 500]) <
                         CustomList([45, 92, 178, 23]))
        self.assertFalse(CustomList([500]) < CustomList([100, 150, 250]))

    def test_le(self):
        """Tests 'low than or equal to' comparison of CustomList instances."""
        self.assertTrue(CustomList([45, 92, 178, 23]) <= CustomList([1000]))
        self.assertFalse(CustomList([500, 500]) <=
                         CustomList([45, 92, 178, 23]))
        self.assertTrue(CustomList([500]) <= CustomList([100, 150, 250]))

    def test_eq(self):
        """Tests 'equal to' comparison of CustomList instances."""
        self.assertTrue(CustomList([45, 92, 178, 22])
                        == CustomList([45, 92, 178, 22]))
        self.assertTrue(CustomList([45, 92, 178, 22])
                        == CustomList([45, 92, 177, 23]))
        self.assertTrue(CustomList([68, 92, 178]) ==
                        CustomList([45, 92, 178, 23]))
        self.assertTrue(CustomList([45, 92, 178, 23])
                        == CustomList([68, 92, 178]))
        self.assertFalse(CustomList([1, 45, 6]) == CustomList([1, 46, 6]))

    def test_ne(self):
        """Tests 'not equal to' comparison of CustomList instances."""
        self.assertFalse(CustomList([1, 2, 3]) != CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) != CustomList([5, 1]))
        self.assertTrue(CustomList([1, 2, 3]) != CustomList([2, 30]))

    def test_gt(self):
        """Tests 'greater than' comparison of CustomList instances."""
        self.assertTrue(CustomList([1, 2, 4]) > CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) > CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2]) > CustomList([1, 2, 3]))

    def test_ge(self):
        """Tests 'low than or equal to' comparison of CustomList instances."""
        self.assertTrue(CustomList([1, 2, 4]) >= CustomList([1, 2, 3]))
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2]) >= CustomList([1, 2, 3]))

    def test_addition_dif_types(self):
        """Tests correctness of different types addition."""
        self.assertEqual(list(CustomList([23, 41, 96]) +
                         [92, 4]), list(CustomList([115, 45, 96])))
        self.assertEqual(list(CustomList(
            [100, -40, 96])+[92, 4, 6, 10]), list(CustomList([192, -36, 102, 10])))
        self.assertEqual(list([92, 4]+CustomList([23, 41, 96])),
                         list(CustomList([115, 45, 96])))
        self.assertEqual(list([92, 4, 150, -43]+CustomList([3, 37, -10])),
                         list(CustomList([95, 41, 140, -43])))

    def test_subtraction_dif_types(self):
        """Tests correctness of different types subtraction."""
        self.assertEqual(list(CustomList([23, 41, 96]) -
                         [92, 4]), list(CustomList([-69, 37, 96])))
        self.assertEqual(list(CustomList([100, -40, 96]) -
                         [92, 4, 6, 10]), list(CustomList([8, -44, 90, -10])))
        self.assertEqual(list([92, 4]-CustomList([23, 41, 96])),
                         list(CustomList([69, -37, -96])))
        self.assertEqual(list([92, 4, 150, -43]-CustomList([3, 37, -10])),
                         list(CustomList([89, -33, 160, -43])))

    def test_addition(self):
        """Extra tests of addition's corectness."""
        self.assertEqual(list(CustomList(
            [5, 1, 3, 7])+CustomList([1, 2, 7])), list(CustomList([6, 3, 10, 7])))
        self.assertEqual(list(CustomList(
            [1])+CustomList([2, 5])), list(CustomList([3, 5])))

    def test_subtraction(self):
        """Extra tests of subtraction's corectness."""
        self.assertEqual(list(CustomList(
            [5, 1, 3, 7])-CustomList([1, 2, 7])), list(CustomList([4, -1, -4, 7])))
        self.assertEqual(list(CustomList(
            [1])-CustomList([2, 5])), list(CustomList([-1, -5])))

    def test_add_incorrect_types(self):
        """Tests incompatibility of types except list and CustomList in addition."""
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
        """Tests incompatibility of types except list and CustomList in subtraction."""
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
