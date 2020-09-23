from dataclasses import dataclass
from typing import Tuple

from bananas.ast.common import quote
from bananas.serializer.node import Node, to_sexpr


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
    value: str

    def to_sexpr(self):
        return self.op, quote(self.name), quote(self.value)


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
