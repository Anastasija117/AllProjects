#Temperature converter

temperature = float(input("Enter the temperature: "))
type = input("Is it celsius or fahrenheit (C or F)?: ")
if type == "C":
    temperature2 = round((9 * temperature) / 5 + 32, 1)
    print(f"{temperature}°C is {temperature2}°F")
elif type == "F":
    temperature2 = round((temperature - 32) * 5 / 9, 1)
    print(f"{temperature}°F is {temperature2}°C")
else:
    print("Error")

end = input("End")