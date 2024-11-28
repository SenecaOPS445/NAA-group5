#!/usr/bin/env python3


if __name__ == '__main__':
#Using while True to keep loop going untill proper input is inputted        
    while True:
        intro = user_input()
        print(intro)
#using if statements for the possible options the user can input and use

        if intro == '1':
            cpu()
            break

        elif intro == '2':
            check_disk_space()
            break

        elif intro == '3':
            memory()
            break
#if the input choice is invalid this error message will show up
        else:
            print("____________________________________")
            print("Invalid Choice. ")
            print("Please choose valid number according to what you want to see")

