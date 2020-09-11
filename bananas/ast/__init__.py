from bananas.ast.branchmonkey.datatypes import ArrayConst, Pointer
from bananas.ast.branchmonkey.mocks import Mock
from bananas.ast.branchmonkey.variables import Argv, Declare
from bananas.ast.branchmonkey.wasi.clock import (
    ClockResGet,
    ClockTimeGet,
    WasiClockTimeData,
)
from bananas.ast.web_assembly.assertions import AssertReturn, AssertTrap
from bananas.ast.web_assembly.datatypes import (
    Float32Const,
    Float64Const,
    Integer32Const,
    Integer64Const,
)
from bananas.ast.web_assembly.invoke import Invoke

nodes = [
    Integer32Const,
    Integer64Const,
    Float32Const,
    Float64Const,
    Invoke,
    AssertReturn,
    AssertTrap,
    Argv,
    Declare,
    Pointer,
    ArrayConst,
    Mock,
    ClockTimeGet,
    ClockResGet,
    WasiClockTimeData,
]

name_to_node = {node.get_op(): node for node in nodes}
