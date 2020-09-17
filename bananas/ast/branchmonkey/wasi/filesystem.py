from dataclasses import dataclass
from typing import Tuple

from bananas.ast.common import quote
from bananas.serializer import Node, to_sexpr


@dataclass
class Filesystem(Node):
    op = "filesystem"
    args: Tuple[str]

    def to_sexpr(self):
        return f";;{(self.op, *map(quote, self.args))}"

    @staticmethod
    def create(*args):
        return Filesystem(args)
