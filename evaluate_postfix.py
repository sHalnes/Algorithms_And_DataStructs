from stack import Stack

''' this function performs operations +, -, /, *'''

def eval_p(expression):
    stack = Stack()
    tokens = expression.split(' ')
    for token in tokens:
        if token == ' ': continue
        if token == '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()


# def evaluate_postfix():
#     print('type in values. press Enter after a value. when finish type "."')
#     stack = Stack()
#     while True:
#         value = eval(input())
#         if value == 'T':
#             break
#         else:
#             stack.push(value)
#         # if value == '+' and not stack.is_empty():
#         #     try:
#         #         stack.push(stack.pop() + stack.pop())
#         #     except: IndexError
#         # # elif value == '-' and not stack.is_empty():
#         # #     try:
#         # #         a = stack.pop()
#         # #         b = stack.pop()
#         # #         stack.push(b - a)
#         # #     except: IndexError
#         # elif value == '.':
#         #     break
#         # else:
#         #     #try:
#         #     value = int(value)
#         #     stack.push(value)
#         #     print('a value pushed')
#         #    # except:
#         #     #    print('something happened')
#     print(stack.pop())
#
# evaluate_postfix()
print(eval_p('56 47 + 2 *'))


def eval_postfix(expr):
    import re
    token_list = re.split("([^0-9])", expr)
    stack = Stack()
    for token in token_list:
        if token == '' or token == ' ':
            continue
        if token == '+':
            sum = stack.pop() + stack.pop()
            stack.push(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        else:
            stack.push(int(token))
    return stack.pop()