"""Unit tests for json parser."""
from unittest.mock import Mock, call, patch
import unittest
from json_parser import parse_json


class TestParser(unittest.TestCase):
    """Test case for json parser."""

    def test_value_error(self):
        """Tests throwing ValueError on empty json."""
        with self.assertRaises(ValueError):
            parse_json(None, print, ["field"], ["keyword"])
        with self.assertRaises(ValueError):
            parse_json('"ab:', print, ["field"], ["keyword"])

    def test_type_error(self):
        """Tests throwing TypeError for None or uncallable arguments."""
        with self.assertRaises(TypeError):
            parse_json('{"a": "b"}', None, ["field"], ["keyword"])
        with self.assertRaises(TypeError):
            not_method = 5
            parse_json('{"a": "b"}', not_method, ["field"], ["keyword"])
        with self.assertRaises(TypeError):
            parse_json('{"a": "b"}', print, keywords=["keyword"])
        with self.assertRaises(TypeError):
            parse_json('{"a": "b"}', print, keywords=None,
                       required_fields=["keyword"])

    def test_calls_callback(self):
        """Tests order of callback calls."""
        callback_mock = Mock(return_value='some result')
        parse_json("""{"first_key": "Uhm-uhm, hello my friend",
                "third": "Nice to meet you!",
                "second_key": "hello and goodbye"}""",
                   callback_mock, ["first_key", "second_key"],
                   ["hello", "goodbye"])

        callback_mock.assert_has_calls(
            [call('first_key', 'hello'),
             call('second_key', 'hello'),
             call('second_key', 'goodbye')])

    @patch('builtins.print')
    def test_correct_words(self, mock_print):
        """Tests correctness of usage callback."""

        def test_callback(*args):
            """Callback function, prints string in upper case."""
            print(("{}:" * len(args)).format(*args).rstrip(':').upper())

        parse_json("""{"Intro": "My name is Gustavo", "Middle": "Uhm.",
        "End": "But you can call me Gas."}""",
                   keyword_callback=test_callback, required_fields=[
                       "Intro", "End"],
                   keywords=["My", "you", "me"])
        expected_calls = [call("INTRO:MY"), call("END:YOU"), call("END:ME")]
        mock_print.assert_has_calls(expected_calls)

    def test_similar_words(self):
        """Tests parser's behavior on similar but not equal words."""
        callback_mock = Mock(return_value='some result')
        parse_json("""{"first_key": "Uhm-uhm, hello my friend",
            "third": "Nice to meet you!",
            "second_key": "hello and goodbye"}""",
                   callback_mock, ["first_key", "second_key"],
                   ["friends", "nice", "uhm"])
        callback_mock.assert_has_calls([])
