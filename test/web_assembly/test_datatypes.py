from test.conftest import validate

from bananas.ast import Float32Const, Float64Const

f32_const = "(f32.const 1)"
f32_const_ast = [Float32Const("1")]


def test_f32_const():
    validate(f32_const, f32_const_ast)


f64_const = "(f64.const 2)"
f64_const_ast = [Float64Const("2")]


def test_f64_const():
    validate(f64_const, f64_const_ast)
