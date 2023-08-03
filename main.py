# import print_tree function from tree_functions file
from tree_functions import print_tree

# input function allows user input
# int function converts a number/string into an integer
height = int(input("Please enter a number for the height of the tree: "))

# lower method returns the lowercase string from the given string by converting each uppercase character to lowercase
# strip method removes any leading and trailing whitespace
has_star = input("Should the tree be drawn with a star on top of it? Please write down (y/n): ").lower().strip() == 'y'

# function to print the tree by using user input
print_tree(height, has_star)
