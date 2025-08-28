
import reader
import printer
import env as environment

def _mk(fn):
    #MAGIC *thunder*
    return reader.Obj(
        reader.Kind._fn, 
        lambda *args: 
            reader.Obj(
                reader.Kind._int, 
                fn(*[x.content for x in args])
            )
    )

repl_env = environment.Env(outer=None)
repl_env.set('+', _mk(lambda a, b: a +  b))
repl_env.set('-', _mk(lambda a, b: a -  b))
repl_env.set('*', _mk(lambda a, b: a *  b))
repl_env.set('/', _mk(lambda a, b: a // b))



def READ(x):
    return reader.read_str(x)

def EVAL(obj, env):
    match obj.kind:
        case reader.Kind._sym:
            return env.get(obj.content)

        case reader.Kind._list if len(obj.content) > 0:
            match obj.content:
                case [sym, key, target] if sym.content == 'def!':
                    value = EVAL(target, env)
                    env.set(key.content, value)
                    return value

                case [sym, bindings, target] if sym.content == 'let*':
                    inner = environment.Env(env)

                    keys = bindings.content[ ::2]
                    vals = bindings.content[1::2]
                    for (key, val) in zip(keys, vals):
                        inner.set(key.content, EVAL(val, inner))

                    return EVAL(target, inner)

                case l:
                    fn, *args = [EVAL(x, env) for x in l]
                    return fn.content(*args)

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

