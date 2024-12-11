def create_stack():
    # Creates a stack
    stack = []
    return stack
 
def is_empty(stack):
    # Checks if the stack is empty, returns True or False
    return len(stack) == 0
 
def push(stack, item):
    # Appends an item to the end of a stack
    stack.append(item)
 
def pop(stack):
    # Pops the end of a stack, removing it from the end and storing that data
    if is_empty(stack):
        return None
    return stack.pop()
 
 
def reverse_string(string):
    # Reverses the string using a stack
    stack = create_stack()
    reversed_string = ""
 
    # Uses Push to transfer the string characters to a stack
    for char in string:
        push(stack, char)
 
    # Reverse the stack
    while not is_empty(stack):
        reversed_string += pop(stack)
    return reversed_string
 
 
def get_user_input():
    # User Input
    user_input = input("Enter a string to reverse: ")
    return user_input
 
def main():
    user_input = get_user_input()
    reversed_string = reverse_string(user_input)
    if is_empty(user_input):
        print("String is Empty")
    else:
        print("Reversed String:", reversed_string)
 
main()

