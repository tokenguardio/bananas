from test.conftest import validate

from bananas.ast import (
    AssertReturn,
    ClockResGet,
    ClockTimeGet,
    Integer32Const,
    Integer64Const,
    Invoke,
    WasiClockTimeData,
)

time = """(clock_time_get (i32.const 0) (wasi_clock_time_data (i32.const 28) (i64.const 0)))
(assert_return (invoke "f") (i32.const 28))"""
time_ast = [
    ClockTimeGet(
        Integer32Const("0"),
        (WasiClockTimeData(Integer32Const("28"), Integer64Const("0")),),
    ),
    AssertReturn(Invoke("f", ()), Integer32Const("28")),
]


def test_clock_get_time():
    validate(time, time_ast)


res = """(clock_res_get (i32.const 0) (wasi_clock_time_data (i32.const 28) (i64.const 0)))
(assert_return (invoke "f") (i32.const 28))"""
res_ast = [
    ClockResGet(
        Integer32Const("0"),
        (WasiClockTimeData(Integer32Const("28"), Integer64Const("0")),),
    ),
    AssertReturn(Invoke("f", ()), Integer32Const("28")),
]


def test_clock_get_res():
    validate(res, res_ast)
