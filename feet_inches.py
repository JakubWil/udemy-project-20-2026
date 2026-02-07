feet_inches = input("Enter feet and inches  ")


def parse(feet_inches):
    f,i = feet_inches.split( )
    return f,i



def convert(feet,inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


f,i = parse(feet_inches)
print(f"fi:{f} and {i}")

if convert(f,i) < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")