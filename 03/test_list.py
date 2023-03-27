import unittest
from src.custom_list import CustomList

class TestCustomList(unittest.TestCase):

    def test_add_returned_type(self):
        self.assertIsInstance(CustomList([1, 2, 3])+[4, 8], CustomList)
        self.assertIsInstance([4, 8]+CustomList([1, 2, 3]), CustomList)
        self.assertIsInstance(CustomList(
            [4, 8])+CustomList([1, 2, 3]), CustomList)

    def test_sub_returned_type(self):
        self.assertIsInstance(CustomList([1, 2, 3])-[4, 8], CustomList)
        self.assertIsInstance([4, 8]-CustomList([1, 2, 3]), CustomList)
        self.assertIsInstance(CustomList(
            [4, 8])-CustomList([1, 2, 3]), CustomList)

    def test_str(self):
        self.assertEqual(str(CustomList()), "Items: []; Sum: 0")
        self.assertEqual(
            str(CustomList([1, 3, -5])), "Items: [1, 3, -5]; Sum: -1")
        self.assertEqual(
            str(CustomList([-1, -4, 3, 2])), "Items: [-1, -4, 3, 2]; Sum: 0")

    def test_lt(self):
        self.assertTrue(CustomList([45, 92, 178, 23]) < CustomList([1000]))
        self.assertFalse(CustomList([500, 500]) <
                         CustomList([45, 92, 178, 23]))
        self.assertFalse(CustomList([500]) < CustomList([100, 150, 250]))

    def test_le(self):
        self.assertTrue(CustomList([45, 92, 178, 23]) <= CustomList([1000]))
        self.assertFalse(CustomList([500, 500]) <=
                         CustomList([45, 92, 178, 23]))
        self.assertTrue(CustomList([500]) <= CustomList([100, 150, 250]))

    def test_eq(self):
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
        self.assertFalse(CustomList([1, 2, 3]) != CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) != CustomList([5, 1]))
        self.assertTrue(CustomList([1, 2, 3]) != CustomList([2, 30]))

    def test_gt(self):
        self.assertTrue(CustomList([1, 2, 4]) > CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2, 3]) > CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2]) > CustomList([1, 2, 3]))

    def test_ge(self):
        self.assertTrue(CustomList([1, 2, 4]) >= CustomList([1, 2, 3]))
        self.assertTrue(CustomList([1, 2, 3]) >= CustomList([1, 2, 3]))
        self.assertFalse(CustomList([1, 2]) >= CustomList([1, 2, 3]))

    def test_addition_dif_types(self):
        self.assertEqual(CustomList([23, 41, 96]) +
                         [92, 4], CustomList([115, 45, 96]))
        self.assertEqual(CustomList(
            [100, -40, 96])+[92, 4, 6, 10], CustomList([192, -36, 102, 10]))
        self.assertEqual([92, 4]+CustomList([23, 41, 96]),
                         CustomList([115, 45, 96]))
        self.assertEqual([92, 4, 150, -43]+CustomList([3, 37, -10]),
                         CustomList([95, 41, 140, -43]))

    def test_subtraction_dif_types(self):
        self.assertEqual(CustomList([23, 41, 96]) -
                         [92, 4], CustomList([-69, 37, 96]))
        self.assertEqual(CustomList([100, -40, 96]) -
                         [92, 4, 6, 10], CustomList([8, -44, 90, -10]))
        self.assertEqual([92, 4]-CustomList([23, 41, 96]),
                         CustomList([69, -37, -96]))
        self.assertEqual([92, 4, 150, -43]-CustomList([3, 37, -10]),
                         CustomList([89, -33, 160, -43]))

    def test_addition(self):
        self.assertEqual(CustomList(
            [5, 1, 3, 7])+CustomList([1, 2, 7]), CustomList([6, 3, 10, 7]))
        self.assertEqual(CustomList(
            [1])+CustomList([2, 5]), CustomList([3, 5]))

    def test_subtraction(self):
        self.assertEqual(CustomList(
            [5, 1, 3, 7])-CustomList([1, 2, 7]), CustomList([4, -1, -4, 7]))
        self.assertEqual(CustomList(
            [1])-CustomList([2, 5]), CustomList([-1, -5]))

    def test_add_incorrect_types(self):
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
