from functools import reduce
# Variant `a`
# sizes = int(input())
# sizes = sizes.strip()
# sizes = sizes.split() # " "
# x = sizes[0]
# y = sizes[1]
# z = sizes[2]

# Variant `b`
# x, y, z = input().strip().split()
# print(f"{x=}, {y=}, {z=}")
# x, y, z = map(int, (x, y, z))
# volume = x * y * z
# print(f"{volume=}")

# Variant `c`
# x, y, z = map(int, input().strip().split())
# volume = x * y * z
# print(f"{volume=}")

# Variant `d`
volume = reduce(
        lambda x, y: x * y,
        map(int, input().strip().split())
        )
print(f"{volume=}")
