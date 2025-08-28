

def put(s):
    print(s, end='')


def pr_str(node, tl=True):
    if type(node) is list:
        put('(') 
        for i, elem in enumerate(node):
            pr_str(elem, tl=False)
            if i != len(node) - 1:
                put(' ')
        put(')') 

    else:
        put(node)

    if tl:
        put('\n')


