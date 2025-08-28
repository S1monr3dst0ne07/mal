
import reader
import printer

def _mk(fn):
    #MAGIC *thunder*
    return lambda *args: reader.Obj(reader.Kind._int, fn(*[x.content for x in args]))

repl_env = {
    '+': _mk(lambda a, b: a +  b),
    '-': _mk(lambda a, b: a -  b),
    '*': _mk(lambda a, b: a *  b),
    '/': _mk(lambda a, b: a // b)
}



def READ(x):
    return reader.read_str(x)

def EVAL(obj, env):
    match obj.kind:
        case reader.Kind._sym:
            try:
                return env[obj.content]
            except KeyError:
                raise Exception(f"Symbol {obj.content} not found")

        case reader.Kind._list if len(obj.content) > 0:
            evald = [EVAL(x, env) for x in obj.content]
            fn, *args = evald
            return fn(*args)

        case _:
            return obj



def PRINT(x):
    printer.pr_str(x)


def rep(x):
    PRINT(EVAL(READ(x), repl_env))


while True:
    try:
        rep(input("user> "))

    except EOFError:
        break

    except Exception as E:
        print(E)

