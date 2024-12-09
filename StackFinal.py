def create_stack():
    # creates an empty stack
    stack = []
    return stack

def is_empty(stack):
    # Checks if the stack is empty
    return len(stack) == 0

def push(stack, item):
    # Pushes an item onto the top of the stack
    stack.append(item)

def pop(stack):
    # Pops and return the top item from the stack
    # Returns None if the stack is empty
    if is_empty(stack):
        return None
    return stack.pop()

def reverse_string(string):
    # Reverses a string using a stack
    # The string input is reversed
    # Returns the reversed string
    stack = create_stack()
    reversed_string = ""

    # Pushes each character of the string on the stack
    for char in string:
        push(stack, char)

    # Pop characters from the stack and append them to the reversed string
    while not is_empty(stack):
        reversed_string += pop(stack)

    return reversed_string

def get_user_input():
    # Prompts the user to enter a string
    user_input = input("Enter a string to reverse: ")
    return user_input

def main():
    # Main function to execute the string reversal process
    user_input = get_user_input()
    reversed_string = reverse_string(user_input)
    print("Reversed string:", reversed_string)

main()
