def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

# def display():
#     print('display function ran')

# decorator_display = decorator_function(display)
# decorator_display()

@decorator_function
def display():
    print('hello world')


display()