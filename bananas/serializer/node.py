from dataclasses import dataclass, fields

from bananas.serializer.stringify import is_list, sexpr_to_str


def to_sexpr(element):
    """Convert commands to list of primitives recursively."""
    if isinstance(element, Node):
        return element.to_sexpr()
    elif is_list(element):
        return tuple(map(to_sexpr, element))
    else:
        return element


class Node:
    op: str

    def __iter__(self):
        """
        Dataclasses are not iterable by default:
        http://github.com/ericvsmith/dataclasses/issues/21#issuecomment-317120601

        Python docs does not explicitly guarantee the order of objects returned by fields():
        http://docs.python.org/3/library/dataclasses.html#dataclasses.fields
        Although fields() is used internally by astuple() and is a public function so it is pretty stable.
        """
        return (getattr(self, field.name) for field in fields(self))

    @classmethod
    def get_op(cls):
        """First field of a dataclass means node type."""
        return cls.op

    @classmethod
    def create(cls, *args, **kwargs):
        """Constructor. Any function specific data preparation can be done here."""
        return cls(*args, **kwargs)

    def to_sexpr(self):
        return self.get_op(), *map(to_sexpr, self)

    def to_string(self):
        """Some nodes are so long they need to customize printing (block instructions)"""
        return sexpr_to_str(self.to_sexpr())
