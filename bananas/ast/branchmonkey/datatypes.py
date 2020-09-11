from dataclasses import dataclass
from typing import List

from bananas.ast.common import quote
from bananas.ast.web_assembly.datatypes import I32
from bananas.serializer import Node, to_sexpr


@dataclass
class ArrayConst(I32):
    op = "array.const"
    size: int


@dataclass
class Pointer(I32):
    op = "pointer"
    name: str

    def to_sexpr(self):
        return self.get_op(), quote(self.name)
