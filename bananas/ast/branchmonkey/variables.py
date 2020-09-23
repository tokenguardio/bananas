from dataclasses import dataclass
from typing import Tuple, Union

from bananas.ast.common import quote
from bananas.ast.webassembly.datatypes import TypeSubOp
from bananas.serializer.node import Node, to_sexpr
from bananas.serializer.stringify import sexpr_to_str


@dataclass
class Declare(Node):
    op = "declare"
    name: str
    values: Tuple[Node]

    @staticmethod
    def create(name, *args):
        return Declare(name, args)

    def to_sexpr(self):
        return self.op, quote(self.name), *map(to_sexpr, self.values)


@dataclass
class Argv(Node):
    op = "argv"
    argv: Tuple[str]

    def to_sexpr(self):
        return self.op, *map(quote, self.argv)

    @staticmethod
    def create(*args):
        return Argv(args)


@dataclass
class Symbol(Node):
    op = "symbol"
    name: str
    value: Union[str, TypeSubOp]

    def to_sexpr(self):
        if isinstance(self.value, TypeSubOp):
            value = self.value.to_sexpr()
        else:
            value = quote(self.value)
        return self.op, quote(self.name), value


@dataclass
class Symbolics(Node):
    op = "symbolics"
    symbols: Tuple[Symbol]

    def to_sexpr(self):
        return self.op, *map(to_sexpr, self.symbols)

    def to_string(self):
        return f";; {super().to_string()}"

    @staticmethod
    def create(*symbols):
        return Symbolics(symbols)
