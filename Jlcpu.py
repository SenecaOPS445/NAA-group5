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


if __name__ == '__main__':
    intro = input("Please enter 'cpu', 'memory': ")
    print(intro)

    if intro == 'cpu':
        cpu()
    elif intro == 'memory':
        memory()
    else:
        print("Invalid option selected.")
