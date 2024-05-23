def repeated_decorator(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            func(*args, **kwargs)
    return wrapper


@repeated_decorator
def example_result(printed_text):
    print(printed_text)


example_result('Print Me!', count=20)
