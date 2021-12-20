# 1234 -> 2345
# abc -> bcd
# ord char
KEY = 1

def coder(txt: str):
    strs = ""
    for i in txt:
        strs += chr(ord(i) + KEY)

    return strs


def decoder(txt: str):
    strs = ""
    for i in txt:
        strs += chr(ord(i) - KEY)
    return strs

print(coder("1234"))  # 2345
print(coder("abc"))  # bcd
print(coder("Alex"))  # bcd

print(decoder("2345"))  # 1234
print(decoder("bcd"))  # abc
print(decoder("Bmfy"))  # Alex
