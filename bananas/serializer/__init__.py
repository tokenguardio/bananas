from bananas.serializer.node import Node, to_sexpr
from bananas.serializer.stringify import sexpr_list_to_str, sexpr_to_str


def serialize_single_node(node: Node) -> str:
    return node.to_string()


def serialize(nodes: [Node]) -> str:
    return "\n".join(map(serialize_single_node, nodes))
