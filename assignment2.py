#!/usr/bin/env python3
#Author: Umar Manjra
umanjra-patch-1
def user_input():
    print("Welcome to the system report tool!")
    print("Please choose an option to display the information:")
    print("1. CPU usage")
    print("2. Disk usage")
    print("3. Memory usage")  # Added memory option
    choice = input("Enter the number of your choice: ").strip().lower()
    return choice

ajpatel44
# Student ID: ajpatel44

import shutil

def check_disk_space(path="/"):
    # Get disk space details
    total, used, free = shutil.disk_usage(path)

    # Convert bytes to human-readable format
    def convert_to_gb(size_in_bytes):
        return size_in_bytes / (1024 ** 3)

    print(f"Disk Space on {path}:")
    print(f"Total: {convert_to_gb(total):.2f} GB")
    print(f"Used: {convert_to_gb(used):.2f} GB")
    print(f"Free: {convert_to_gb(free):.2f} GB")

# Check disk space on root directory
check_disk_space()


#Author= Brandon Yeung
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
          