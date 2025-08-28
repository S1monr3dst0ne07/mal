
import reader
import printer


def READ(x):
    return reader.read_str(x)

def EVAL(x):
    return x

def PRINT(x):
    printer.pr_str(x)


def rep(x):
    PRINT(EVAL(READ(x)))


while True:
    try:
        rep(input("user> "))

    except EOFError:
        break

    except Exception as E:
        print(E)

