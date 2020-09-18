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

    def STRING(self, token):
        return Token.new_borrow_pos(token.type, token.strip('"'), token)


GRAMMAR_PATH = os.path.join(os.path.dirname(__file__), "grammar.lark")
parser = Lark.open(GRAMMAR_PATH, parser="lalr", transformer=CreateAST())
parse = parser.parse
