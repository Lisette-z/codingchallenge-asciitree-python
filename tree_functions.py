# user-defined function with height default value=5, has_star default value=True
# print_tree function gives the opportunity to change the signs for treetop, tree_body, tree_stem into whatever
def print_tree(height=5, has_star=True, treetop="*", tree_body="X", tree_stem="I"):

    # function to check if has_star input is True
    if has_star:

        # function to calculate the position of the star and to print it on top of the tree
        print(" " * (height - 1) + treetop)

    # range function returns a sequence of numbers start=1, stop=input number for the height of the tree +1
    rows = range(1, height+1)

    # for loop function iterate over the items contained within the rows
    for i in rows:

        # x variable to calculate the position of the tree signs
        x = 2 * i - 1

        # y variable to calculate the number of left spaces
        y = height - i

        # function to calculate the position of the left spaces and the "X" in each row and to print it
        print(y * " " + x * tree_body)

    # function to calculate the position of the stem and to print it
    print(" " * (height - 1) + tree_stem)
