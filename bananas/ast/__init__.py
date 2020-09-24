from bananas.ast.branchmonkey.datatypes import (
    Float32Symbolic,
    Float64Symbolic,
    Integer32Symbolic,
    Integer64Symbolic,
    Pointer,
)
from bananas.ast.branchmonkey.mocks import Mock
from bananas.ast.branchmonkey.variables import Argv, Declare, BitVector, KingKong
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
    Integer32Symbolic,
    Integer64Symbolic,
    Float32Symbolic,
    Float64Symbolic,
    KingKong,
    BitVector,
]

name_to_node = {node.get_op(): node for node in nodes}
