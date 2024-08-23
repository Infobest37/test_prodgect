
def test_function(b):
    print("Привет я из пространства имен функции test_function")

    def inner_function(b):
        print("Я область видимости функции test_function")

    inner_function(b)
    return inner_function


print(inner_function)