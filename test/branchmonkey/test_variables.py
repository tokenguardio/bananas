from test.conftest import validate

from bananas import parse, serialize
from bananas.ast import (
    Argv,
    AssertReturn,
    Declare,
    Integer32Const,
    Invoke,
    Pointer,
    BitVector,
    KingKong,
)

declare = """(declare "ptr" (i32.const 16843009) (i32.const 16843009) (i32.const 42))
(assert_return (invoke "foo" (i32.pointer "ptr") (i32.const 2)) (i32.const 1))"""
declare_ast = [
    Declare(
        "ptr",
        (Integer32Const("16843009"), Integer32Const("16843009"), Integer32Const("42")),
    ),
    AssertReturn(
        Invoke("foo", (Pointer("ptr"), Integer32Const("2"))), Integer32Const("1")
    ),
]


def test_declare():
    validate(declare, declare_ast)


argv = r"""(argv "test" "dojpa" "he\"t\`m")
(assert_return (invoke "f" (i32.const 1)) (i32.const 1))"""
argv_ast = [
    Argv(
        (
            "test",
            "dojpa",
            r"he\"t\`m",
        )
    ),
    AssertReturn(Invoke("f", (Integer32Const("1"),)), Integer32Const("1")),
]


def test_argv():
    validate(argv, argv_ast)


kingkong = """(kingkong (bitvec "n" "Lech") (bitvec "m" "Roch"))"""
kingkong_ast = [KingKong((BitVector("n", "Lech"), BitVector("m", "Roch")))]


def test_kingkong():
    # FIXME: Use `validate()` once KingKong is uncommented
    parsed = parse(kingkong)
    assert parsed == kingkong_ast
    assert serialize(parsed) == f";; {kingkong}"
