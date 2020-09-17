from dataclasses import dataclass

from bananas.ast.common import quote
from bananas.ast.webassembly.datatypes import I32
from bananas.serializer import Node, to_sexpr


@dataclass
class Pointer(I32):
    op = "pointer"
    name: str

    def to_sexpr(self):
        return self.get_op(), quote(self.name)
