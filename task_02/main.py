from collections import deque

FILE_PATH = './Calc1.stk'

NUM_TYPE = 'NUM'
OPERATOR_TYPE_MAP = {"*": "STAR", "/": "SLASH", "+": "PLUS", "-": "MINUS"}


def is_number(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def get_operator_type(op):
    return OPERATOR_TYPE_MAP[op]


def is_operator(element):
    return element in ['*', '+', '-', '/']


def tokenize_item(element):
    type = ""
    lexeme = ""
    if(is_number(element)):
        type = NUM_TYPE
        lexeme = element
    elif is_operator(element):
        type = get_operator_type(element)
        lexeme = element
    else:
        raise Exception("Error", f"Unexpected character: {element}")

    token = {"type": type, "lexeme": lexeme}

    print(f"Read token: {str(token)}")

    return token


def get_expression(n1, n2, op):
    expression = f"{n1} {op} {n2}"
    return expression


def exec_expression(exp):
    return eval(exp)


def tokenize_data(data):
    print("----Start tokenize----")
    tokens = []

    for row in data:
        element = row.strip()

        token = tokenize_item(element)
        tokens.append(token)

    print("----End tokenize----")
    return tokens


def parse_rpn(data):
    print("----Start parsing----")
    stack = deque()

    for token in data:
        type = token["type"]
        lexeme = token["lexeme"]

        if type == NUM_TYPE:
            print(f"Read number: {lexeme}")
            stack.append(lexeme)
        elif type in OPERATOR_TYPE_MAP.values():
            print(f"Read operand: {lexeme}")
            n2 = stack.pop()
            n1 = stack.pop()

            exp = get_expression(n1, n2, lexeme)
            result = exec_expression(exp)
            print(f"Executed expression: '{exp}' = {result}")
            stack.append(result)
        else:
            raise Exception("Unkown Type", type)

    final_result = stack.pop()

    if len(stack) != 0:
        raise Exception("Stack not empty at end of operation")

    print("----End parsing----")
    return final_result


data = None
with open(FILE_PATH, 'r') as f:
    data = f.read().split('\n')

tokens = tokenize_data(data)
result = parse_rpn(tokens)
print("Resultado Final")
print(result)
