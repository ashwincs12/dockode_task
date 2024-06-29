import math
def pattern(rows, columns):
    top = " ___ "
    middle = "/   \\"
    bottom = "\\___/"
    alt_top="___"
    space="   "


    modified_cols= math.ceil(columns/2)

    print(rows,"\t",columns)

    for row in range(rows):

        # Printing top portion of hexagon (Applicable for only first row)
        if row==0:
            for col in range(modified_cols):
                print(top + space, end="")
            print()


        # Printing middle portion of hexagon
        for col in range(modified_cols):
            #Hexagons in last column does not need the alt_top part
            if(col==modified_cols-1):
                print(middle, end="")
                continue
            #Other hexagons (not in the last column) need the middle part and alt_top part
            print(middle + alt_top, end="")
        print()

        #Printing bottom part of the hexagon
        for col in range(modified_cols):
            print(bottom+space,end="")
        print()

rows=int(input("Enter number of rows: "))
columns=int(input("Enter number of columns: "))
pattern(rows, columns)

