from bananas import parse, serialize
from bananas.ast import Argv, AssertReturn, Integer32Const, Invoke

comment = """;; (invoke "__original_main")
;; model_count=1
(argv "asda")
(assert_return (invoke "__original_main") (i32.const 1))
;; 2020-09-12 21:51:21.219859
"""
comment_ast = [
    Argv(("asda",)),
    AssertReturn(Invoke("__original_main", ()), Integer32Const("1")),
]
comment_serialized = """(argv "asda")
(assert_return (invoke "__original_main") (i32.const 1))"""


def test_one_line_comments_are_ignored():
    parsed = parse(comment)
    assert parsed == comment_ast
    assert serialize(parsed) == comment_serialized
