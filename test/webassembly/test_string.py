from bananas.parser import parse
from bananas import serialize

from bananas.ast import Argv


def validate(s, expected_parsed, expected_serialized):
    parsed = parse(s, start="string")
    assert parsed == expected_parsed
    node = Argv(argv=[parsed])
    serialized = serialize([node])
    assert serialized == f"(argv {expected_serialized})"


def test_control_sequences():
    s = '"\\t\\n\\r\\\\\\\'\\""'
    validate(s, "\t\n\r\\'\"", s)


def test_unicode_sequence():
    s = '"\\u{798f}"'

    # serialized value is not \u{798f}, but 福 - parse and serialize are not inverse when unicode sequences are present, by design
    validate(s, "福", '"福"')
