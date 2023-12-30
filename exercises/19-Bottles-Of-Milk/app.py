# ✅↓ Write your code here. ↓✅


def number_of_bottles():
    for x in range(99, 0, -1):
        if x == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk.")
        elif x == 2:
            print("2 bottles of milk on the wall, 2 bottles of milk.")
            print("Take one down and pass it around, 1 bottle of milk on the wall.")
        elif x == 3:
            print("3 bottles of milk on the wall, 3 bottles of milk.")
            print("Take one down and pass it around, 2 bottles of milk on the wall.")
        elif x == 0:
            print("No more bottles of milk on the wall, no more bottles of milk.")
            print("Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(f"{x} bottles of milk on the wall, {x} bottles of milk.")
            print(f"Take one down and pass it around, {x-1} bottles of milk on the wall.")

number_of_bottles()
