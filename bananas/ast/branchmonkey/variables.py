from dataclasses import dataclass
from typing import Tuple

from bananas.ast.branchmonkey.datatypes import ArrayConst, Pointer
from bananas.ast.common import quote
from bananas.serializer.node import Node


@dataclass
class Declare(Node):
    op = "declare"
    name: Pointer
    value: ArrayConst


@dataclass
class Argv(Node):
    op = "argv"
    argv: Tuple

    def to_sexpr(self):
        return self.op, *map(quote, self.argv)

    @staticmethod
    def create(*args):
        return Argv(args)
