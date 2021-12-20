X = "X"
O = "0"
B = "_"  # Blank
base_1 = []


def print_field(field):
    for i in field:
        print(i[0], i[1], i[2])


def get_status_field(field):
    # if field[0][0] == field[1][1] == field[2][2]:
    #     return 1 if field[1][1] == X else 2
    for i in field:
        if B in i:
            return -1


def is_valid(n_put):
    if n_put.isdigit() == None:
        print("input contains letter")
        return None
    if len(n_put) != 1:
        print("input contains more than one digit")
        return None
    if int(n_put) < 1:
        print("a negative number or 0 is entered")
        return None

    if n_put not in base_1:
        if n_put == "1":

            return 0, 0
        if n_put == "2":
            return 0, 1
        if n_put == "3":
            return 0, 2
        if n_put == "4":
            return 1, 0
        if n_put == "5":
            test = (1,1)
            return test
        if n_put == "6":
            return 1, 2
        if n_put == "7":
            return 2, 0
        if n_put == "8":
            return 2, 1
        if n_put == "9":
            return 2, 2
    if n_put in base_1:
        print("в базе уже есть")
        return "exit"
    else:
        print("Unknown error")
        return None


print(base_1)


def game():
    first_player = True
    field = [
        [B, B, B],
        [B, B, B],
        [B, B, B]
    ]

    while True:
        n_put = input("Enter sector from 1 to 9 ")

        if is_valid(n_put) == None:
            continue
        else:
            base_1.append(is_valid(n_put))
            test2 = is_valid(n_put)

        x, y = test2
        if first_player == True:
            first_player = False
            field[x][y] = X
        else:
            first_player = True
            field[x][y] = O

        game_status = get_status_field(field)
        print_field(field)

        if game_status != -1:
            break


if __name__ == "__main__":
    game()
