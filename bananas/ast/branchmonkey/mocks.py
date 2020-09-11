from dataclasses import astuple, dataclass, field
from functools import partial
from typing import List

from bananas.serializer.node import Node


@dataclass
class Mock(Node):
    op = "mock"
    function_name: str
    data: List[Node]
