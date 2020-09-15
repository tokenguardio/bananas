""" Mocks clock_res_get and clock_time_get """
from dataclasses import dataclass
from functools import partial
from typing import List, Union

from bananas.ast.branchmonkey.mocks import Mock
from bananas.ast.common import quote
from bananas.ast.webassembly.datatypes import Integer32Const, Integer64Const
from bananas.serializer import Node, to_sexpr


@dataclass
class WasiClockTimeData(Node):
    """
    Used by clock_res_get and clock_time_get.
    For more info see WASI specification:
    http://github.com/blockhunters/wasi-libc/blob/master/libc-bottom-half/headers/public/wasi/api.h
    And C documentation:
    http://linux.die.net/man/3/clock_gettime
    """

    op = "wasi_clock_time_data"

    # Value returned by function (success or error code)
    return_value: Union[Integer32Const, "z3.BitVecNumRef"]
    # Time/Resolution in nanoseconds
    tv_nsec: Union[Integer64Const, "z3.BitVecNumRef"]


@dataclass
class ClockGet(Node):
    """WasiClockTimeData alongside clock it is generated for"""

    clock_id: Integer32Const
    data: List

    @classmethod
    def create(cls, clock_id, *data):
        return cls(clock_id, data)

    def to_sexpr(self):
        return self.get_op(), to_sexpr(self.clock_id), *map(to_sexpr, self.data)


class ClockTimeGet(ClockGet):
    op = "clock_time_get"


class ClockResGet(ClockGet):
    op = "clock_res_get"
