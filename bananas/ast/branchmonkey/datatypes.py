from dataclasses import dataclass

from bananas.ast.common import quote
from bananas.ast.webassembly.datatypes import F32, F64, I32, I64
from bananas.serializer import Node, to_sexpr


@dataclass
class Pointer(I32):
    op = "pointer"
    name: str

    def to_sexpr(self):
        return self.get_op(), quote(self.name)


@dataclass
class Symbolic:
    op = "symbolic"


class Integer32Symbolic(I32, Symbolic):
    pass


class Integer64Symbolic(I64, Symbolic):
    pass


class Float32Symbolic(F32, Symbolic):
    pass


class Float64Symbolic(F64, Symbolic):
    pass
