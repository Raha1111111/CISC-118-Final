def countdown(n):
    """
    Recursively counts down from n to 1 and then prints "Blastoff!".

    Parameters:
        n (int): The starting number for the countdown.
    """
    # Base case: if n is less than 1, print "Blastoff!" and return.
 if n < 1:
        print("Blastoff!")

    # Recursive case: print the current number and call countdown with the next lower number
    else:
        print(n)
        countdown(n - 1)

# Example usage
countdown(10)
