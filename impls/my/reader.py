
import re

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


def read_form(reader):
    match reader.peek()[0]:
        case '(':
            return read_list(reader)
        case '"':
            return read_string(reader) 
        case _:
            return read_atom(reader)

def read_string(reader):
    return reader.next()


def read_list(reader):
    reader.expect('(')

    acc = []
    while reader.peek() != ')':
        acc.append(read_form(reader))

    reader.expect(')')
    return acc

def read_atom(reader):
    tok = reader.next()
    
    if tok.isdigit(): return int(tok)
    else            : return tok

