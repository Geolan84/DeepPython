"""Unit tests for resume descriptors."""
import unittest
from descriptors import Data


class TestDescriptors(unittest.TestCase):
    """Test case for resume descriptors."""

    def test_telegram_incorrect_type(self):
        """Tests incorrect type (not str) for telegram."""
        with self.assertRaises(TypeError):
            resume = Data(telegram=404)
        resume = Data()
        with self.assertRaises(TypeError):
            resume.telegram = 404

    def test_telegram_negative(self):
        """Tests length, At Sign and no_spaces conditions."""
        with self.assertRaises(ValueError):
            resume = Data(telegram='@tel')
        resume = Data()
        with self.assertRaises(ValueError):
            resume.telegram = '@tel'
        with self.assertRaises(ValueError):
            resume.telegram = '@teleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeegram'
        with self.assertRaises(ValueError):
            resume.telegram = 'WithoutAtSign'
        with self.assertRaises(ValueError):
            resume.telegram = '@With Space'

    def test_del_telegram(self):
        """Tests delete telegram method."""
        resume = Data(telegram="@LaninGM")
        self.assertEqual(resume.telegram, "@LaninGM")
        del resume.telegram
        with self.assertRaises(AttributeError):
            print(resume.telegram)

    def test_telegram_positive(self):
        """Tests telegram set and get correctness."""
        resume = Data(telegram="@LaninGM")
        self.assertEqual(resume.telegram, "@LaninGM")
        resume.telegram = "@RamonAntonio"
        self.assertEqual(resume.telegram, "@RamonAntonio")

    def test_experience_incorrect_type(self):
        """Tests incorrect (not int) type for experience field."""
        with self.assertRaises(TypeError):
            resume = Data(experience="404")
        resume = Data()
        with self.assertRaises(TypeError):
            resume.experience = "404"

    def test_experience_non_negative(self):
        """Tests negative values in experience field."""
        with self.assertRaises(ValueError):
            resume = Data(experience=-3)
        resume = Data()
        with self.assertRaises(ValueError):
            resume.experience = -1
        with self.assertRaises(ValueError):
            resume.experience = -10

    def test_experience_positive(self):
        """Tests experience set and get correctness."""
        resume = Data(experience=5)
        self.assertEqual(resume.experience, 5)
        resume.experience += 1
        self.assertEqual(resume.experience, 6)

    def test_del_experience(self):
        """Tests del method for experience."""
        resume = Data(experience=10)
        self.assertEqual(resume.experience, 10)
        del resume.experience
        with self.assertRaises(AttributeError):
            print(resume.experience)

    def test_qualification_incorrect_type(self):
        """Tests incorrect type for qualification."""
        with self.assertRaises(TypeError):
            Data(qualification=101)
        resume = Data()
        with self.assertRaises(TypeError):
            resume.qualification = 101
        with self.assertRaises(TypeError):
            resume.qualification = []

    def test_qualification_incorrect_value(self):
        """Tests not existing values for qualification."""
        with self.assertRaises(ValueError):
            Data(qualification="Invalid qualification")
        resume = Data()
        with self.assertRaises(ValueError):
            resume.qualification = "Invalid qualification"

    def test_qualifiction_positive(self):
        """Tests qualification set and get correctness."""
        resume = Data(qualification='Middle')
        self.assertEqual(resume.qualification, 'Middle')
        resume.qualification = 'Lead'
        self.assertEqual(resume.qualification, 'Lead')
        resume.qualification = 'Senior'
        self.assertEqual(resume.qualification, 'Senior')

    def test_del_qualification(self):
        """Tests """
        resume = Data(qualification='Intern')
        self.assertEqual(resume.qualification, 'Intern')
        del resume.qualification
        with self.assertRaises(AttributeError):
            print(resume.qualification)
