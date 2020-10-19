from dataclasses import dataclass, field

from bananas.serializer.node import Node


def quote(value):
    return f'"{value}"'


def escape(value):
    return str.translate(
        value,
        {
            ord("\t"): "\\t",
            ord("\n"): "\\n",
            ord("\r"): "\\r",
            ord('"'): '\\"',
            ord("'"): "\\'",
            ord("\\"): "\\\\",
        },
    )
