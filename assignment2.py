#!/usr/bin/env python3
#Author: Umar Manjra
#umanjra-patch-1
def user_input():
    print("Welcome to the system report tool!")
    print("Please choose an option to display the information:")
    print("1. CPU usage")
    print("2. Disk usage")
    print("3. Memory usage")  # Added memory option
    choice = input("Enter the number of your choice: ").strip().lower()
    return choice



#jli638-patch-1
def cpu():
    import os

    # Execute the 'top' command and read the output
    cpu_info_line = os.popen("top -bn1 | grep 'Cpu(s)'").readline()
    
    # Sample output: '%Cpu(s):  2.0 us,  1.0 sy,  0.0 ni, 96.7 id,  0.2 wa,  0.0 hi,  0.1 si,  0.0 st'
    # Split the line into tokens to parse the idle CPU percentage
    tokens = cpu_info_line.replace(',', '').split()
    idle_index = tokens.index('id')
    idle_cpu = float(tokens[idle_index - 1])
    
    # Calculate used CPU percentage
    used_cpu = 100 - idle_cpu
    
    # Create a progress bar
    bar_length = 20  # Total length of the progress bar
    filled_length = int(bar_length * used_cpu // 100)
    bar = '[' + '#' * filled_length + ' ' * (bar_length - filled_length) + f' | {used_cpu:.0f}%]'
    
    print(f'CPU Usage      {bar}')


def memory():
    import os
    mem_info = os.popen("free -h").read()
    print('Here is the Memory information:')
    print(mem_info)
        

#ajpatel44
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
          

