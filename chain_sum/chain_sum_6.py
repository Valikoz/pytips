from functools import reduce


class ChainSum(int):
    def __call__(self, value=0):
        return ChainSum(self + value)

# print(1 + ChainSum(5))  # 6
# print(1 + ChainSum(5)(2))  # 8
# print(1 + ChainSum(5)(100)(-10))  # 96

# value = reduce(
#     lambda x, y: ChainSum(x)(y),
#     range(5)
# )
# print(f"{value=}")

value = reduce(
    lambda x, y: ChainSum(x)(y),
    [a for a in range(10) if a%2 == 1]   # test if an integer is odd
)
print(f"{value=}")
