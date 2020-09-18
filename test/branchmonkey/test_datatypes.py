from test.conftest import validate

from bananas.ast import (
    Float32Symbolic,
    Float64Symbolic,
    Integer32Symbolic,
    Integer64Symbolic,
)

i32_symbolic = "(i32.symbolic)"
i32_symbolic_ast = [Integer32Symbolic()]


def test_i32_symbolic():
    validate(i32_symbolic, i32_symbolic_ast)


i64_symbolic = "(i64.symbolic)"
i64_symbolic_ast = [Integer64Symbolic()]


def test_i64_symbolic():
    validate(i64_symbolic, i64_symbolic_ast)


f32_symbolic = "(f32.symbolic)"
f32_symbolic_ast = [Float32Symbolic()]


def test_f32_symbolic():
    validate(f32_symbolic, f32_symbolic_ast)


f64_symbolic = "(f64.symbolic)"
f64_symbolic_ast = [Float64Symbolic()]


def test_f64_symbolic():
    validate(f64_symbolic, f64_symbolic_ast)
