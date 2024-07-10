def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
fahrenheit_temperature = 98.6
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
print(f"{fahrenheit_temperature} Fahrenhei0t is {celsius_temperature:.2f}Celsius.")
celsius_temperature = 37
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} Celsius is {fahrenheit_temperature:.2f}Fahrenheit.")