from dataclasses import dataclass
from typing import Any

from bananas.ast.common import quote
from bananas.ast.webassembly.invoke import Invoke
from bananas.serializer.node import Node, to_sexpr


@dataclass
class AssertReturn(Node):
    op = "assert_return"
    invoke: Invoke
    expected_result: Any


@dataclass
class AssertTrap(Node):
    op = "assert_trap"
    invoke: Invoke
    msg: str

    @staticmethod
    def create(invoke, msg):
        return AssertTrap(invoke, msg)

    def to_sexpr(self):
        return self.op, to_sexpr(self.invoke), quote(self.msg)
