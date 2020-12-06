def superhero_name_generator():
    print("Welcome to the superhero name generator:\nTo choose your name follow the instructions below")
    first_part = input("Please enter the name of your power. ")
    second_part = input("Please enter the name of your pet or your favorite mythical creature (Ie. Dragon). ")
    superhero_name = first_part + " " + second_part
    return superhero_name


while True:
    name = superhero_name_generator()
    print("your superhero name is {}".format(name))
    print("If you want to generate another name please press 1 to quit press 0")
    if int(input()) == 0:
        break

print("Go out and save the world", name)
