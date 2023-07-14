def chain_sum(number):
    result = number
    def wrapper(number2=None):
        nonlocal result
        try:
            number2 = int(number2)
        except TypeError:
            return print(result)
        result += number2
        return wrapper
    return wrapper

chain_sum(5)()  # 5
chain_sum(5)(2)()  # 7
chain_sum(5)(100)(-10)()  # 95
