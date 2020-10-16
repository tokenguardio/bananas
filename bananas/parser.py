import os

from lark import Lark, Token, Transformer

from bananas.ast import name_to_node


class CreateAST(Transformer):
    def start(self, children):
        return children

    def expr(self, elements):
        if elements == []:
            return elements

        op, *args = elements
        node = name_to_node[op.value]
        return node.create(*args)

    def INT(self, token):
        return Token.new_borrow_pos(token.type, int(token), token)

    def FLOAT(self, token):
        return Token.new_borrow_pos(token.type, float(token), token)

    def HEX_NUM(self, token):
        return Token.new_borrow_pos(token.type, int(token, 16), token)

    def escaped_unicode(self, list):
        assert len(list) == 1
        codepoint = int(list[0])

        # TODO error handling
        assert codepoint < 0xD800 or (codepoint >= 0xE000 and codepoint < 0x110000)
        return chr(codepoint)

    def ESCAPED_CHAR(self, token):
        return Token.new_borrow_pos(
            token.type,
            {
                "\\t": "\t",
                "\\n": "\n",
                "\\r": "\r",
                '\\"': '"',
                "\\'": "'",
                "\\\\": "\\",
            }[str(token)],
            token,
        )

    def string(self, tokens):
        return "".join(tokens)


GRAMMAR_PATH = os.path.join(os.path.dirname(__file__), "grammar.lark")
parser = Lark.open(
    GRAMMAR_PATH, parser="lalr", transformer=CreateAST(), start=["start", "string"]
)


def parse(text, start="start"):
    return parser.parse(text, start)
