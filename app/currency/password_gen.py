import random
import string


def password_generates(lens: int = 10):
    if not isinstance(lens, int):
        raise TypeError("Эй шо дЭлаешЬ нэ тот тип!!")
    result = ""
    choices = string.ascii_letters + string.digits + "!@#$%^&*"
    for i in range(lens):
        result += random.choice(choices)
    return result


if __name__ == "__main__":
    print(password_generates(35))
