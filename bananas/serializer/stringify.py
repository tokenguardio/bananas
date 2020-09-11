from functools import partial
from typing import Generator


def is_list(sexpr):
    sexpr_is = partial(isinstance, sexpr)
    return sexpr_is(list) or sexpr_is(tuple) or sexpr_is(Generator)


def sexpr_to_str(sexpr):
    return f"({sexpr_list_to_str(sexpr)})" if is_list(sexpr) else str(sexpr)


def sexpr_list_to_str(sexprs):
    return " ".join(map(sexpr_to_str, sexprs))
