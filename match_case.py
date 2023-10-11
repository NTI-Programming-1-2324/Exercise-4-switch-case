

# D-pads

d_pad_input = input("Enter D-pad input: ")

match d_pad_input:
    case "Up":
        print("Plauer clicked up")
    case "Down":
        print("Player clicked down")
    case "Left":
        print("Player clicked left")
    case "Right":
        print("Player clicked right")
    case _:
        print("Player clicked none")


# Kontrollknappar

control_input = input("Enter control button input: ")

match control_input:
    case "X":
        print("Player clicked X")
    case "Y":
        print("Player clicked Y")
    case "A":
        print("Player clicked A")
    case "B":
        print("Player clicked B")
    case _:
        print("Player clicked none")

