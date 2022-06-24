def doubler_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@doubler_decorator
def printer_func(name):
    return print(name)


printer_func("Olek")
