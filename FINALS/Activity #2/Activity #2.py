from LinkedStack import LinkedStack
from PositionalList import PositionalList

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    operators = LinkedStack()
    postfix = []
    expression = expression.replace('−', '-')
    tokens = []
    temp = ""
    for char in expression.replace(" ", ""):
        if char.isdigit() or (char == '.' and temp and temp[-1].isdigit()):
            temp += char
        else:
            if temp:
                tokens.append(temp)
                temp = ""
            tokens.append(char)
    if temp:
        tokens.append(temp)

    for token in tokens:
        if token.isdigit() or '.' in token:
            postfix.append(token)
        elif token == '(':
            operators.push(token)
        elif token == ')':
            while not operators.is_empty() and operators.top() != '(':
                postfix.append(operators.pop())
            if operators.is_empty():
                raise ValueError("Mismatched parentheses in the expression.")
            operators.pop()
        else:
            while not operators.is_empty() and precedence[operators.top()] >= precedence[token]:
                postfix.append(operators.pop())
            operators.push(token)

    while not operators.is_empty():
        if operators.top() == '(':
            raise ValueError("Mismatched parentheses in the expression.")
        postfix.append(operators.pop())

    return ' '.join(postfix)

if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter a valid infix expression: ")
            result = infix_to_postfix(expression)
            print(f"postfix: {result}")
            break
        except ValueError as e:
            print("Please try again.")
        except Exception as e:
            print("Please try again.")

print()

def insertionSort(P, ascending=True):
    if len(P) <= 1:
        return

    elements = []
    current = P.first()
    while current:
        elements.append(current.element())
        current = P.after(current)


    for i in range(1, len(elements)):
        key = elements[i]
        j = i - 1
        while j >= 0 and (key < elements[j] if ascending else key > elements[j]):
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = key


    P._header._next = P._trailer
    P._trailer._prev = P._header
    P._size = 0
    for elem in elements:
        P.add_last(elem)


if __name__ == "__main__":
    P = PositionalList()
    print("Original List:")


    P.add_first(1)
    P.add_last(72)
    P.add_last(81)
    P.add_last(25)
    P.add_last(65)
    P.add_last(91)
    P.add_last(11)
    print(P)


    insertionSort(P, ascending=True)
    print("Sorted in Ascending Order:")
    print(P)


    insertionSort(P, ascending=False)
    print("Sorted in Descending Order:")
    print(P)

