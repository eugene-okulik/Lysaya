def finish_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("finished")
        return result
    return wrapper


@finish_decorator
def example_result(printed_text):
    print(printed_text)


example_result('Print Me!')
