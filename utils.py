def prompt() -> int:
    choice = -1
    while choice < 0 or choice > 10:
        print("Select which item would you like the Pal-Bot to work on: ")
        print("0. Pal Sphere")
        print("1. Mega Sphere")
        print("2. Giga Sphere")
        print("3. Arrows")
        print("4. Fire arrows")
        print("5. Nails")
        print("6. Cement")
        print("7. Low Grade Medical Supplies")
        print("8. Medical Supplies")
        print("9. High Grade Medical Supplies")
        print("10. EXIT")
        choice = int(input(": "))

    if choice == 10:
        exit(0)

    return choice


def match_failed(step_id: int):
    match step_id:
        case 0:
            print("\n=== FAILED ACTION: Pal-bot failed to located item on item menu === ")
        case 1:
            print("\n=== FAILED ACTION: Pal-bot failed to located 'MAX' button === ")
        case 2:
            print("\n=== FAILED ACTION: Pal-bot failed to located 'Start production' button === ")
        case _:
            print("\n=== FAILED ACTION: Invalid failure === ")
