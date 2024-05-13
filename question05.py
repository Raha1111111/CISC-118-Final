# Define the width and height of the rectangle
width = 10
height = 10

# Loop through each row
for row in range(height):
    # Initialize an empty string for the row
    line = ""
    # Loop through each column in the row
    for col in range(width):
        # Alternate between '*' and '+' starting with '*' in even rows, '+' in odd rows
        if (row + col) % 2 == 0:
            line += "*"
        else:
            line += "+"
    # Print the completed row
    print(line)
