
import reader
import printer


def _mk_fn(fn):
    return reader.Obj(
        reader.Kind._fn, 
        fn
    )
    

def _mk_int(fn):
    return _mk_fn(
        lambda *args: 
            reader.Obj(
                reader.Kind._int, 
                fn(*[x.content for x in args])
            )
    )

def _mk_bool(fn):
    return _mk_fn(
        lambda *args: 
            _bool(
                fn(*[x.content for x in args])
            )
    )


def _bool(x):
    return reader.Obj(reader.Kind._true if x else reader.Kind._false)

def fn_prn(x):
    printer.pr_str(x)
    return reader.Obj(reader.Kind._nil)

def fn_list(*args):
    return reader.Obj(reader.Kind._list, list(args))

def fn_list_q(x):
    return _bool(x.kind == reader.Kind._list)

def fn_empty_q(x):
    return _bool(len(x.content) == 0)

def fn_count(x):
    count = len(x.content) if x.kind == reader.Kind._list else 0
    return reader.Obj(reader.Kind._int, count)


def fn_equal(a, b):
    return _bool(\
        (a.content == b.content) and \
        (a.kind    == b.kind))


ns = {
    '+': _mk_int(lambda a, b: a +  b),
    '-': _mk_int(lambda a, b: a -  b),
    '*': _mk_int(lambda a, b: a *  b),
    '/': _mk_int(lambda a, b: a // b),
    'prn':    _mk_fn(fn_prn),
    'list':   _mk_fn(fn_list),
    'list?':  _mk_fn(fn_list_q), 
    'empty?': _mk_fn(fn_empty_q),
    'count':  _mk_fn(fn_count), 
    '=':  _mk_fn(fn_equal),
    '<':  _mk_bool(lambda a, b: a < b),
    '>':  _mk_bool(lambda a, b: a > b),
    '<=': _mk_bool(lambda a, b: a <= b),
    '>=': _mk_bool(lambda a, b: a >= b),
}
