from ArrayStack import ArrayStack as Stack

def is_matched(expr):
    '''Return True if all delimiters are properly matched; otherwise, False'''
    left_symbols = '({['
    right_symbols = ')}]'
    stack = Stack()

    for char in expr:
        if char in left_symbols:
            stack.push(char)
        elif char in right_symbols:
            if stack.is_empty():
                return False
            if right_symbols.index(char) != left_symbols.index(stack.pop()):
                return False

    return stack.is_empty()
while True:
    user_input = input("Enter your expression (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break

    if is_matched(user_input):
        print("The symbols are balanced!")
    else:
        print("The symbols are imbalanced!")

def reverse_file(filename):
    '''Reverses the lines of a file using a Stack Data Structure'''
    stack = Stack()
    with open(filename, 'r') as file:
        for line in file:
            stack.push(line)
    with open(filename, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop())
reverse_file('myfile.txt')
print("File content reversed successfully!")

