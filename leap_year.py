def leap_year():

    if (año % 4 == 0) and ((año % 100 != 0) or (año % 400 == 0)):
        return True
    else:
        return False

año = int(input("Ingrese un año: "))

if leap_year():
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")
