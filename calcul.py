def text_to_stack(text: str) -> list:
    """
    take the text input, split with ' ' characters and return it as a list
    ex : "10 12 +" -> ['10', '12', '+']

    :param text: str - the input str
    :return: list - the stack
    """
    text = text.replace('+', ' + ')
    text = text.replace('-', ' -')
    text = text.replace('*', ' * ')
    text = text.replace('/', ' / ')

    stack = text.split(" ")
    stack = [i for i in stack if i != '']
    return stack


def check_element(item: str) -> float or str or Exception:
    """
    check if the element is a float or an operator among ['+', '-', '*', '/']
    if not, raise an Exception

    :param item: str - the input string
    :return: int or str or Exception
    """
    try:
        a = float(item)
        return a
    except ValueError:
        if item in ['+', '-', '*', '/']:
            return item
        else:
            raise Exception(f"Error character: {item}")


def make_operation_from_stack(stack: list[str]) -> float:
    """
    take a stack as input and make the operation according to the Reverse Polish notation
    ex: "10 12 + 20 -" -> 2

    :param stack: list[str] - stack input for the operation
    :return: float - operation output
    """
    temp_stack = []

    while stack:
        item = stack.pop(0)
        item = check_element(item)

        if item in ['+', '-', '*', '/']:
            if len(temp_stack) < 2:
                raise Exception(f"operation error - check at character: {item}")

            a = temp_stack.pop()
            b = temp_stack.pop()
            if item == '+':
                temp_stack.append(a + b)
            elif item == '-':
                temp_stack.append(b - a)
            elif item == '*':
                temp_stack.append(a * b)
            elif item == '/':
                temp_stack.append(b / a)
        else:
            temp_stack.append(item)

    if len(temp_stack) != 1:
        raise Exception("operation error")

    return temp_stack[0]


def make_operation(text: str) -> float:
    """
    convert text as list, then use make_operation_from_stack to make the operation
    :param text: text: str - the input operation as str
    :return: float - operation output
    """
    return make_operation_from_stack(text_to_stack(text))