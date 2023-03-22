from unittest.mock import Mock, call, patch
import unittest
from src.parser import parse_json


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
            a = 5
            parse_json('{"a": "b"}', a, ["field"], ["keyword"])
        with self.assertRaises(TypeError):
            parse_json('{"a": "b"}', print, keywords=[
                       "keyword"], required_field=None)
        with self.assertRaises(TypeError):
            parse_json('{"a": "b"}', print, keywords=None,
                       required_field=["keyword"])

    def test_calls_callback(self):
        """Tests order of callback calls."""
        callback_mock = Mock(return_value='some result')
        parse_json("""{"first_key": "Uhm-uhm, hello my friend",
            "third": "Nice to meet you!", "second_key": "hello and goodbye"}""",
                   callback_mock, ["first_key", "second_key"],
                   ["hello", "goodbye"])

        callback_mock.assert_has_calls(
            [call('hello'), call('hello'), call('goodbye')])

    @patch('builtins.print')
    def test_correct_words(self, mock_print):
        """Tests correctness of usage callback."""

        def test_callback(arg: str):
            """Callback function, prints string in upper case."""
            arg = arg.upper()
            print(arg)

        parse_json('{"Intro": "My name is Gustavo", "Middle": "Uhm.", "End": "But you can call me Gas."}',
                   keyword_callback=test_callback, required_fields=[
                       "Intro", "End"],
                   keywords=["My", "you", "me"])
        expected_calls = [call("MY"), call("YOU"), call("ME")]
        mock_print.assert_has_calls(expected_calls)


    def test_similar_words(self):
        """Tests parser's behavior on similar but not equal words."""
        callback_mock = Mock(return_value='some result')
        parse_json("""{"first_key": "Uhm-uhm, hello my friend",
            "third": "Nice to meet you!", "second_key": "hello and goodbye"}""",
                   callback_mock, ["first_key", "second_key"],
                   ["friends", "nice", "uhm"])
        callback_mock.assert_has_calls([])
