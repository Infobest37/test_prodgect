
def test_function():
    print("Привет я из пространства имен функции test_function")

    def inner_function():
        print("Я область видимости функции test_function")

    inner_function()
    return inner_function


print(test_function())