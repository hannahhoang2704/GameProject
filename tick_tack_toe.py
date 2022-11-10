table = {
    "a1": " ",
    "a3": " ",
    "a2": " ",
    "b1": " ",
    "b2": " ",
    "b3": " ",
    "c1": " ",
    "c2": " ",
    "c3": " ",
}


def check_win(letter):
    if table["a1"] == letter and table["a2"] == letter and table["a3"] == letter:
        print(f"Player {letter} wins")
        return False
    elif table["b1"] == letter and table["b2"] == letter and table["b3"] == letter:
        print(f"Player {letter} wins")
        return False
    elif table["c1"] == letter and table["c2"] == letter and table["c3"] == letter:
        print(f"Player {letter} wins")
        return False
    elif table["c1"] == letter and table["b2"] == letter and table["a3"] == letter:
        print(f"Player {letter} wins")
        return False
    elif table["c3"] == letter and table["b2"] == letter and table["a1"] == letter:
        print(f"Player {letter} wins")
        return False
    elif table["a1"] == letter and table["b1"] == letter and table["c1"] == letter:
        print(f"Player {letter} wins")
        return False
    elif table["a2"] == letter and table["b2"] == letter and table["c2"] == letter:
        print(f"Player {letter} wins")
        return False
    elif table["a3"] == letter and table["b3"] == letter and table["c3"] == letter:
        print(f"Player {letter} wins")
        return False
    else:
        return True


game_on = True
display_table = f"""
        1   2   3 
    a | {table["a1"]} | {table["a2"]} | {table["a3"]} |
    b | {table["b1"]} | {table["b2"]} | {table["b3"]} |
    c | {table["c1"]} | {table["c2"]} | {table["c3"]} |

    """
print(display_table)

count = 0
while game_on:
    x_location = input("Player X: Pick a row and column (e.g. a1, a2, etc.): ").lower()
    check_x = True
    while check_x:
        if table[x_location] == " ":
            table[x_location] = "X"
            count += 1
            check_x = False
        else:
            x_location = input("That is an invalid spot. Please try again: ").lower()
            check_x = True

    display_table = f"""
        1   2   3 
    a | {table["a1"]} | {table["a2"]} | {table["a3"]} |
    b | {table["b1"]} | {table["b2"]} | {table["b3"]} |
    c | {table["c1"]} | {table["c2"]} | {table["c3"]} |

    """

    print(display_table)

    game_on = check_win("X")
    if game_on == False:
        break

    if count >= 9:
        print("There is no winner")
        break

    o_location = input("Player O: Pick a row and column (e.g. a1, a2, etc.): ")
    check_o = True
    while check_o:
        if table[o_location] == " ":
            table[o_location] = "O"
            count += 1
            check_o = False
        else:
            y_location = input("That is an invalid spot. Please try again: ").lower()
            check_o = True

    display_table = f"""
        1   2   3 
    a | {table["a1"]} | {table["a2"]} | {table["a3"]} |
    b | {table["b1"]} | {table["b2"]} | {table["b3"]} |
    c | {table["c1"]} | {table["c2"]} | {table["c3"]} |

    """
    print(display_table)

    game_on = check_win("O")
    if game_on == False:
        break