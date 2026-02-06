feet_inches = input("Enter feet and inches  ")


def convert(feet_inches):
    f,i = feet_inches.split( )
    return f,i



def printing(arg1,arg2):
    print(arg1,arg2)


f,i = convert(feet_inches)
printing(f,i)