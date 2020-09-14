# Bananas

Specification of branchmonkey API. Used by branchmonkey producer and consumers. Includes parser and serializer.

## Installation
Make virtual env
```python -m venv .venv && source .venv/bin/activate```
Install dependencies
```pip install poetry && poetry install```

## Testing
Run command
```pytest```

## Usage

### Parsing
```python
from bananas import parse
from bananas.ast import Argv, AssertReturn
from bananas.ast.web_assembly.datatypes import I32, I64


program = r""";; (invoke "__original_main")
;; model_count=1
(argv "testo" "dojpa" "he\"t\`m")
(assert_return (invoke "f" (i32.const 1)) (i32.const 1))
;; 2020-09-12 21:51:21.219859
"""


def execute_argv(node):
    print('ARGV')
    for arg in node.argv:
        print(arg)


def get_type(node):
    if isinstance(node, I32) or isinstance(node, I64):
        return "Integer"
    return "Float"


def execute_assert_return(node):
    print(f"{node.invoke.function} returns: {get_type(node.expected_result)}")


def execute(nodes):
    for node in nodes:
        ast_to_execution[type(node)](node)


ast_to_execution = {
    Argv: execute_argv,
    AssertReturn: execute_assert_return
}


parsed = parse(program)
execute(parsed)
```

### Serializing
```python
from bananas import serialize
from bananas.ast import Argv, AssertReturn, Invoke, Integer32Const


ast = [
    Argv(("testo", "dojpa", r"he\"t\`m")),
    AssertReturn(Invoke("f", (Integer32Const(1),)), Integer32Const(1)),
]

print(serialize(ast))
```
