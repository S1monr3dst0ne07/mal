
import reader


def put(s):
    print(s, end='')


def pr_str(obj, tl=True):
    match obj.kind:
        case reader.Kind._int: put(obj.content)
        case reader.Kind._sym: put(obj.content)
        case reader.Kind._str: 
            put('"')
            put(obj.content)
            put('"')

        case reader.Kind._list:
            put('(') 
            for i, elem in enumerate(obj.content):
                pr_str(elem, tl=False)
                if i != len(obj.content) - 1:
                    put(' ')
            put(')') 

        case reader.Kind._nil:   put('nil')
        case reader.Kind._true:  put('true')
        case reader.Kind._false: put('false')
        case reader.Kind._fn:    put('#<function>')
    
    if tl:
        put('\n')


