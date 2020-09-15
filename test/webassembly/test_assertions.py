from test.conftest import validate

from bananas.ast import AssertReturn, AssertTrap, Integer32Const, Integer64Const, Invoke

assert_return = '(assert_return (invoke "f") (i64.const 28))'
assert_return_ast = [AssertReturn(Invoke("f", ()), Integer64Const("28"))]


def test_assert_return():
    validate(assert_return, assert_return_ast)


assert_trap = '(assert_trap (invoke "div" (i32.const 2147483654) (i32.const 20)) "signed division by zero")'
asssert_trap_ast = [
    AssertTrap(
        Invoke("div", (Integer32Const("2147483654"), Integer32Const("20"))),
        "signed division by zero",
    )
]


def test_assert_trap():
    validate(assert_trap, asssert_trap_ast)
