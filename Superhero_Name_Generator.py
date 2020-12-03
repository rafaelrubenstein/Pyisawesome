def superhero_name_generator():
    print("Welcome to the superhero name generator:\nTo choose your name follow the instructions below")
    first_part = input("Please enter the name of the city you grew up in. ")
    second_part = input("Please enter the name of your pet or your favorite mythical creature (Ie. Dragon). ")
    superhero_name = first_part + second_part
    print("your superhero name is {}".format(superhero_name))


end = '-'
while end != 0:
    superhero_name_generator()
    print("If you want to generate another name please press 1 to quit press 0")
    end = int(input())
else:
    print("Go out and save the world")
