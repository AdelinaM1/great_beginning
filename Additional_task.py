def minimum_number():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    if (a < b) and (a < c):
        minimum = a
    elif (b < a) and (b < c):
        minimum = b
    else:
        minimum = c

    return minimum

print("The minimum number is", minimum_number())
# comment
