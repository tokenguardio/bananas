from dataclasses import dataclass, field

from bananas.serializer.node import Node


def quote(value):
    return f'"{value}"'
