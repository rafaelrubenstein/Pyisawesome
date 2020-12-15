# This program allows user to enter data, and create a new clone of this data.The data is then reversed and another clone is created.

def clone(x):
    if x == type(str):
        print(x)
    else:
        new_x = x[:]
        return new_x


def reverse_clone(x):
    if x == type(str):
        reverse_x = x.reverse()
        print(reverse_x)
    else:
        new_x = x[::-1]
        return new_x


x = input("Please enter a string tuple or list:\n")
print(clone(x))
print(reverse_clone(x))
