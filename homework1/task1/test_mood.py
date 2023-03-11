from src.mood import predict_message_mood, SomeModel
from unittest import mock
import unittest


class TestMood(unittest.TestCase):
    def setUp(self):
        self.model = SomeModel()


    def test_parameters(self):
        with mock.patch("src.mood.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5
            with self.assertRaises(ValueError):
                predict_message_mood(None, self.model, 0.2, 0.6)
            with self.assertRaises(ValueError):
                predict_message_mood("", self.model, 0.2, 0.6)
            with self.assertRaises(ValueError):
                predict_message_mood("Hello", None, 0.2, 0.6)
            with self.assertRaises(ValueError):
                predict_message_mood("Hello", self.model, 0.7, 0.6)
            with self.assertRaises(ValueError):
                predict_message_mood("Hello", self.model, 0.7, 1.6)
            with self.assertRaises(ValueError):
                predict_message_mood("Hello", self.model, -0.1, 0.6)
            self.assertEqual(mock_predict.call_count, 0)


    def test_predict_positive(self):
        with mock.patch("src.mood.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.333
            self.assertEqual("неуд", predict_message_mood("Cat", self.model, 0.4, 0.7))
            self.assertEqual("норм", predict_message_mood("Cat", self.model, 0.2, 0.4))
            self.assertEqual("отл", predict_message_mood("Cat", self.model, 0.2, 0.3))

    def test_boundaries(self):
        with mock.patch("src.mood.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.2
            self.assertEqual("норм", predict_message_mood("Hello", self.model, 0.2, 0.4))
            self.assertEqual("норм", predict_message_mood("Hello", self.model, 0.1, 0.2))

