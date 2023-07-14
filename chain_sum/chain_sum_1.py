def chain_sum(number: int):
    result = number
    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return print(result)
        result += number2
        return wrapper
    return wrapper

chain_sum(5)()  # 5
chain_sum(5)(2)()  # 7
chain_sum(5)(100)(-10)()  # 95
