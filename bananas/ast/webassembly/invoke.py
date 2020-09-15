from dataclasses import dataclass
from typing import Tuple

from bananas.ast.common import quote
from bananas.serializer.node import Node, to_sexpr


@dataclass
class Invoke(Node):
    op = "invoke"
    function: str
    args: Tuple[Node]

    @staticmethod
    def create(function_name, *args):
        return Invoke(function_name, args)

    def to_sexpr(self):
        return (self.op, quote(self.function), *map(to_sexpr, self.args))
