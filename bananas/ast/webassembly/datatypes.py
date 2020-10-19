from dataclasses import dataclass, field
from typing import Any

from bananas.ast.common import quote
from bananas.serializer.node import Node


class TypeSubOp(Node):
    val_type: str
    op: str

    @classmethod
    def get_op(cls):
        return f"{cls.val_type}.{cls.op}"

    @classmethod
    def create(cls, token=None):
        if token != None:
            return cls(str(token))
        return cls()


@dataclass
class ConstValue:
    op = "const"
    value: Any


class I32(TypeSubOp):
    val_type = "i32"


class I64(TypeSubOp):
    val_type = "i64"


class F32(TypeSubOp):
    val_type = "f32"


class F64(TypeSubOp):
    val_type = "f64"


class Integer32Const(ConstValue, I32):
    pass


class Integer64Const(ConstValue, I64):
    pass


class Float32Const(ConstValue, F32):
    pass


class Float64Const(ConstValue, F64):
    pass
