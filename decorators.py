
# def test(fun):
#     def wrapper(*args, **kwargs):
#         print("Initial world of python")
#         fun(*args, **kwargs)
#     return wrapper


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello Mr/Mrs.")
        func(*args, **kwargs)
        print(f"Welcome to python tuts")

    return wrapper


# @decorator
# @test
def name(a):
    print(a)


b = name("Bhushan Chaudhari")

result = decorator(name)
print(result(b))
