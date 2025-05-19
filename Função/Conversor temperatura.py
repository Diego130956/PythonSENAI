def conversor_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin
def conversor_Fahrenheit(celsius):
    Farhenheit = celsius * 1.8 + 32
    return Farhenheit




celsius = int(input('Digite o graus celsus atual'))

print('O graul em Fahrenheit é', conversor_Fahrenheit(celsius))
print('O raul em Kelvin é', conversor_kelvin(celsius))