import enum
from typing import NoReturn, Never
# from typing import assert_never


def sum_two_ints(a: int, b: int) -> int:
    return a + b

def print_sum_two_ints(a: int, b: int) -> None:
    print(sum_two_ints(a, b))

print("result is", print_sum_two_ints(10, 20)) #result is None

print(type(None))

def always_raise() -> NoReturn:
    raise RuntimeError("Oh-oh")

def assert_never(_: Never) -> NoReturn:
    raise AssertionError("Expected to be unreachable")

class Gender(enum.Enum):
    MALE = "male",
    FEMALE = "female",
    TRACTOR = "tractor"

def handle_incorrect_password(user_gender: Gender) -> None:
    message = "Sorry, {}, you wrote incorrect password"
    match user_gender:
        case Gender.MALE:
            entered = "man"
        case Gender.FEMALE:
            entered = "baby"
        case _ as unreachable:
            assert_never(unreachable)
    print(message.format(entered))

def main() -> None:
    # always_raise()
    print("Bye")
