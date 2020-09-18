from bananas.serializer.node import Node, to_sexpr


def serialize_single_node(node: Node) -> str:
    return node.to_string()


def serialize(nodes: [Node]) -> str:
    return "\n".join(map(serialize_single_node, nodes))
