def user_input():
    print("Welcome to the system report tool!")
    print("Please choose an option to display the information:")
    print("1. CPU usage")
    print("2. Disk usage")
    print("3. Memory usage")  # Added memory option
    choice = input("Enter the number of your choice: ").strip().lower()
    return choice