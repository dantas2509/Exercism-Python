def is_paired(input_string):
    pairs = {'[': ']', '{': '}', '(': ')'}
    stack = list()

    for char in input_string:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False

    return not stack  # if stack is empty return True else False
