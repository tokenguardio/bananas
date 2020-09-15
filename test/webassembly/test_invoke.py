from test.conftest import validate

from bananas.ast import Integer32Const, Integer64Const, Invoke

invoke_no_args = '(invoke "f")'
invoke_no_args_ast = [Invoke("f", ())]


def test_invoke_no_args():
    validate(invoke_no_args, invoke_no_args_ast)


invoke_args = '(invoke "f" (i32.const 1) (i64.const 5))'
invoke_args_ast = [Invoke("f", (Integer32Const("1"), Integer64Const("5")))]


def test_invoke_args():
    validate(invoke_args, invoke_args_ast)
