



def READ(x):
    return x

def EVAL(x):
    return x

def PRINT(x):
    return x


def rep(x):
    return READ(EVAL(PRINT(x)))


while True:
    try:
        print(rep(input("user> ")))

    except EOFError:
        break

