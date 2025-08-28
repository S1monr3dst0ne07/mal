
import re
import typing
from enum import Enum, auto
from dataclasses import dataclass

class Kind(Enum):
    _list = auto()
    _int  = auto()
    _str  = auto()
    _sym  = auto()


@dataclass
class Obj:
    kind : Kind
    content : typing.Any



class Reader:
    def __init__(self, stream):
        self.stream = stream
        self.pos = 0
        self.len = len(stream)

    def peek(self):
        if self.len == self.pos:
            raise Exception("EOF")

        token = self.stream[self.pos]
        return token

    def next(self):
        token = self.peek()
        self.pos += 1
        return token

    def expect(self, cont):
        token = self.next()
        if cont != token:
            raise Exception(f"Expected {cont} but got {token}")



def tokenize(src):
    tok_raw = re.findall(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)""", src)
    return list(filter(lambda x: len(x) > 0, tok_raw))


def read_str(src):
    stream = tokenize(src)
    reader = Reader(stream)
    return read_form(reader)


def read_form(reader) -> Obj:
    match reader.peek()[0]:
        case '(':
            return read_list(reader)
        case '"':
            return read_string(reader) 
        case _:
            return read_atom(reader)

def read_string(reader) -> Obj:
    content = reader.next().strip('"')
    return Obj(Kind._str, content)


def read_list(reader) -> Obj:
    reader.expect('(')

    acc = []
    while reader.peek() != ')':
        acc.append(read_form(reader))

    reader.expect(')')
    return Obj(Kind._list, acc)

def read_atom(reader) -> Obj:
    tok = reader.next()
    
    if tok.isdigit(): return Obj(Kind._int, int(tok))
    else            : return Obj(Kind._sym, tok)

