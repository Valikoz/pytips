names = ["John", "Adam", "Max", "Arnold", "Jessica"]

# Variant `a`
names_starts_a = []
for name in names:
    if name.startswith("A"):
        names_starts_a.append(name)
print(names_starts_a)

# Variant `b`
names_starts_a = [name for name in names if name.startswith("A")]
print(names_starts_a)

# Variant `c`
names_starts_a = filter(lambda name: name.startswith("A"), names)
print(tuple(names_starts_a))
