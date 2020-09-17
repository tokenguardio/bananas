from bananas.ast.branchmonkey.datatypes import Pointer
from bananas.ast.branchmonkey.mocks import Mock
from bananas.ast.branchmonkey.variables import Argv, Declare
from bananas.ast.branchmonkey.wasi.clock import (
    ClockResGet,
    ClockTimeGet,
    WasiClockTimeData,
)
from bananas.ast.branchmonkey.wasi.filesystem import Filesystem
from bananas.ast.webassembly.assertions import AssertReturn, AssertTrap
from bananas.ast.webassembly.datatypes import (
    Float32Const,
    Float64Const,
    Integer32Const,
    Integer64Const,
)
from bananas.ast.webassembly.invoke import Invoke
from bananas.serializer import Node

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
    Mock,
    ClockTimeGet,
    ClockResGet,
    WasiClockTimeData,
    Filesystem,
]

name_to_node = {node.get_op(): node for node in nodes}
