import json
import re

def _validate_parsing_args(json_str: str, keyword_callback, required_fields, keywords):
    """Checks arguments of method for parsing"""
    if not json_str:
        raise ValueError("Empty json is not valid!")
    if required_fields is None:
        raise TypeError("Requaired fields should be not None!")
    if keywords is None:
        raise TypeError("keywords should be not None!")
    if keyword_callback is None or not callable(keyword_callback):
        raise TypeError("Callback FUNCTION is obligatory!")
    

def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    """Parse json string, search special words and execute callback."""
    _validate_parsing_args(json_str, keyword_callback, required_fields, keywords)
    try:
        json_doc = json.loads(json_str)
    except json.JSONDecodeError:
        raise ValueError("Corrupted JSON!")
    for field in required_fields:
        for keyword in keywords:
            for key, value in json_doc.items():
                if key == field:
                    for _ in range(re.split(' |\.|,|!|\?|:', value).count(keyword)):
                        keyword_callback(keyword)
