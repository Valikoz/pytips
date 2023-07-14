def chain_sum(number):
    def wrapper(number2=None):
        if number2 is None:
            return print(wrapper.result)
        wrapper.result += number2
        return wrapper
    wrapper.result = number
    return wrapper

chain_sum(5)()  # 5
chain_sum(5)(2)()  # 7
chain_sum(5)(100)(-10)()  # 95
