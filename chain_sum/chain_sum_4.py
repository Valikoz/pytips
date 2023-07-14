def chain_sum(number):
    def wrapper(number2=None):
        def inner():
            wrapper.result += number2
            return wrapper
        logic = {
            type(None): lambda: print(wrapper.result),
            int: inner
        }
        return logic[type(number2)]()
    wrapper.result = number
    return wrapper

chain_sum(5)()  # 5
chain_sum(5)(2)()  # 7
chain_sum(5)(100)(-10)()  # 95
