# Decorators in Python

# A decorator is a function that takes another function as input,
# adds additional behavior to it, and returns a modified function.


def greeting_decorator(original_function):

    # This wrapper function adds extra behavior before and after
    # the execution of the original function.
    def wrapper():
        print("The function is about to run.")
        original_function()
        print("The function has finished executing.")

    return wrapper


# A simple function that prints a greeting
def say_hello():
    print("Hello, Soumadip!")


# Applying the decorator manually
decorated_function = greeting_decorator(say_hello)

# Calling the decorated function
decorated_function()


# Another way to apply a decorator is by using the @decorator syntax.
# This automatically wraps the function with the decorator.


@greeting_decorator
def say_goodbye():
    print("Goodbye, Soumadip!")


# Calling the decorated function
say_goodbye()


# Decorators that accept arguments


# This decorator repeats the execution of a function multiple times.
def repeat(number_of_times):

    def decorator(function_to_repeat):

        def wrapper(name):
            for i in range(number_of_times):
                function_to_repeat(name)

        return wrapper

    return decorator


# Applying the decorator with an argument
@repeat(3)
def greet_person(name):
    print(f"Hello, {name}!")


# Calling the decorated function
greet_person("Soumadip")
