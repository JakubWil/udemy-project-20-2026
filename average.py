def average_temp():
    with open("temps.txt", "r") as file:
        temps = file.readlines()
        values = temps[1:]
        values = [float(i) for i in values]

    average = sum(values) / len(values)
    return average



print(f"The average temperature is: {average_temp():.2f}°C")