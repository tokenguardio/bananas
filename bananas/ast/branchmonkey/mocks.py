from dataclasses import astuple, dataclass, field
from functools import partial
from typing import Tuple

from bananas.serializer.node import Node


@dataclass
class Mock(Node):
    op = "mock"
    function_name: str
    data: Tuple[Node]
