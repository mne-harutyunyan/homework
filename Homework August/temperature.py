# Store functions for converting temperatures between Celsius, Fahrenheit, and Kelvin 
# in a dictionary.Write a function convert_temperature(value, from_unit, to_unit) 
# that uses this dictionary to perform the conversion.
def cel_to_far(x):
    return (x * 9 / 5) + 32
def cel_to_kel(x):
    return x + 273.15
def far_to_kel(x):
    return (x - 32) * 5/9 + 273.15
def far_to_cel(x):
    return (x- 32) * 5/9
def kel_to_cel(x):
    return x - 273.15
def kel_to_far(x):
    return (x - 273.15) * 9/5 + 32 


def convert_temperature(value, from_unit, to_unit):
    dict = {
        ("celsus", "farenheit"): cel_to_far,
        ("celsus" , "kelvin"): cel_to_kel,
        ("farenheit" , "kelvin"): far_to_kel,
        ("farenheit" , "celsus"): far_to_cel,
        ("kelvin" , "celsus") : kel_to_cel,
        ("kelvin" , "farenheit") : kel_to_far
    }
    units = dict[from_unit,to_unit]
    res = units(value)
    return res
value = int(input("Enter the value: "))
from_unit = input("Enter from which unit you want to convert the value: ")
to_unit = input("Enter to which unit you want to convert the value: ")

print(convert_temperature(value,from_unit, to_unit))