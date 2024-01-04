from sys import argv

def add_arguments():
    # Get the arguments and calculate the sum
    arguments = argv[1:]  # Exclude the script name
    sum_result = sum(int(arg) for arg in arguments)

    # Print the result
    print(sum_result)

# Call the function to add and print the result
if __name__ == "__main__":
    add_arguments()
