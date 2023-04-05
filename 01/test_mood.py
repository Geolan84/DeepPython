"""Unit tests for "predict_message_mood" method."""
from unittest import mock
import unittest
from mood_predictor import predict_message_mood, SomeModel


class TestMood(unittest.TestCase):
    """Test case to check "predict_message_mood" method."""

    def setUp(self):
        """Creates instance of model for tests."""
        self.model = SomeModel()

    def test_parameters(self):
        """Tests exceptions from method and count of calls for mock."""
        with mock.patch("mood_predictor.SomeModel.predict") as mock_predict:
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
        """Tests correctness of conditions by different areas."""
        with mock.patch("mood_predictor.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.333
            self.assertEqual("неуд", predict_message_mood(
                "Cat", self.model, 0.4, 0.7))
            self.assertEqual("норм", predict_message_mood(
                "Cat", self.model, 0.2, 0.4))
            self.assertEqual("отл", predict_message_mood(
                "Cat", self.model, 0.2, 0.3))

    def test_boundaries(self):
        """Tests boundaries of conditions."""
        with mock.patch("mood_predictor.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.2
            self.assertEqual("норм", predict_message_mood(
                "Hello", self.model, 0.2, 0.4))
            self.assertEqual("норм", predict_message_mood(
                "Hello", self.model, 0.1, 0.2))
            mock_model.return_value = 0.0
            self.assertEqual("неуд", predict_message_mood(
                "Hello", self.model, 0.3, 0.7))
            mock_model.return_value = 1.0
            self.assertEqual("отл", predict_message_mood(
                "Hello", self.model, 0.3, 0.7))
            
    def test_predict_called_once(self):
        with mock.patch("mood_predictor.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.3
            predict_message_mood("SomeArgIsHere", self.model)
            mock_model.assert_called_once()

    def test_predict_arguments(self):
        with mock.patch("mood_predictor.SomeModel.predict") as mock_model:
            mock_model.return_value = 0.4
            predict_message_mood("FirstArg", self.model)
            mock_model.assert_called_with("FirstArg")
            predict_message_mood("SecondArg", self.model)
            mock_model.assert_called_with("SecondArg")
