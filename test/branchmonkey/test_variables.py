from test.conftest import validate

from bananas.ast import (
    Argv,
    ArrayConst,
    AssertReturn,
    Declare,
    Integer32Const,
    Invoke,
    Pointer,
)

declare = """(declare (i32.pointer "my_ptr") (i32.array.const 3))
(assert_return (invoke "foo" (i32.pointer "my_ptr") (i32.const 5)) (i32.const 0))"""
declare_ast = [
    Declare(Pointer("my_ptr"), ArrayConst("3")),
    AssertReturn(
        Invoke("foo", (Pointer("my_ptr"), Integer32Const("5"))), Integer32Const("0")
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
