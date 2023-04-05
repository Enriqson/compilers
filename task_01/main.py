from collections import deque

FILE_PATH = './Calc1.stk'


def is_number(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def is_operator(element):
    return element in ['*', '+', '-', '/']


def get_expression(n1, n2, op):
    expression = f"{n1} {op} {n2}"
    return expression


def exec_expression(exp):
    return eval(exp)


def parse_rpn(data):
    stack = deque()

    for row in data:
        element = row.strip()

        if is_number(element):
            print(f"Read number: {element}")
            stack.append(element)
        elif is_operator(element):
            print(f"Read operand: {element}")
            n2 = stack.pop()
            n1 = stack.pop()
            exp = get_expression(n1, n2, element)
            result = exec_expression(exp)
            print(f"Executed expression: '{exp}' = {result}")
            stack.append(result)
        else:
            print(element)
            raise Exception("Not a valid expression")

    final_result = stack.pop()

    if len(stack) != 0:
        raise Exception("Stack not empty at end of operation")
    return final_result


data = None
with open(FILE_PATH, 'r') as f:
    data = f.read().split('\n')

result = parse_rpn(data)
print("Resultado Final")
print(result)
