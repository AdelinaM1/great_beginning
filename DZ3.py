
a = int(input("Give me 1st number: "))
b = int(input("Give me 2nd number: "))
def compare(a,b):

    if (a < b):
        print(f"Oh, no it looks like {a} is smaller than {b} :(")
    elif (a > b):
        print(f"{a} is bigger than {b}.")
    else:
        print("WOW! They are equal!!")

compare(a,b)
