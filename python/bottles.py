num: int = int(input("How many bottles of beer? "))

for i in range(num, -1, -1):
    # Prints the song lyrics. If [i == 1], then "bottle" is used instead.
    print(f"{i} {"bottles" if i != 1 else "bottle"} of beer on the wall, {i} {"bottles" if i != 1 else "bottle"} of beer.")

    if i != 0:
        print(f"Take one down and pass it around, {i - 1} {"bottles" if i - 1 != 1 else "bottle"} of beer on the wall.")
    # When 0 bottles are left, the last paragraph sentence changes to this.
    else:
        print(f"Go to the store and buy some more, {num} {"bottles" if num != 1 else "bottle"} of beer on the wall.")
