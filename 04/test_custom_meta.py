"""Unit tests for custom metaclass."""
import unittest
from custom_meta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    """Inheritor of metaclass"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        """Some method."""
        return "line result"

    def __str__(self):
        return "Custom_by_metaclass"


class TestMetaClass(unittest.TestCase):
    """Test case for custom metaclass."""

    def setUp(self):
        """Creates instance of custom class for tests."""
        self.custom = CustomClass()

    def test_call_with_custom(self):
        """Tests availability of existing attribute with custom prefix."""
        self.assertEqual(self.custom.custom_x, 50)
        self.assertEqual(self.custom.custom_line(), "line result")

    def test_call_without_custom(self):
        """Tests unavailability of existing attribute without custom prefix."""
        with self.assertRaises(AttributeError):
            self.custom.x
        with self.assertRaises(AttributeError):
            self.custom.line()

    def test_dynamic_with_custom(self):
        """Tests availability of new attribute with custom prefix"""
        self.custom.new_attr = "new attribute"
        self.assertEqual(self.custom.custom_new_attr, "new attribute")

    def test_dynamic_without_custom(self):
        """Tests unavailability of new attribute with custom prefix."""
        self.custom.new_attr = "new attribute"
        with self.assertRaises(AttributeError):
            self.custom.new_attr

    def test_magic_methods(self):
        """Tests availability of magic methods without custom prefix."""
        self.assertEqual(self.custom.__str__(), "Custom_by_metaclass")
        self.assertEqual(self.custom.__module__, "test_custom_meta")

    def test_private_attribute(self):
        """Tests private attributes."""
        self.custom.__new_private_attribute = 112
        with self.assertRaises(AttributeError):
            self.custom.__new_private_attribute
        with self.assertRaises(AttributeError):
            self.custom._TestMetaClass__new_private_attribute
        self.assertEqual(
            self.custom.custom__TestMetaClass__new_private_attribute, 112)

    def test_protected_attribute(self):
        """Tests protected attributes."""
        self.custom._new_protected_attribute = 112
        with self.assertRaises(AttributeError):
            self.custom._new_protected_attribute
        self.assertEqual(self.custom.custom__new_protected_attribute, 112)
