from bananas import parse, serialize


def validate(as_str, as_ast):
    parsed = parse(as_str)
    assert parsed == as_ast
    assert serialize(parsed) == as_str
