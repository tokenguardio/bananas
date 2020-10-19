from bananas import parse, serialize


def validate(as_str, as_ast, start="start"):
    parsed = parse(as_str, start)
    assert parsed == as_ast
    assert serialize(parsed) == as_str
