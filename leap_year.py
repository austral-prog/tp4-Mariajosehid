def leap_year():

    if (año % 4 == 0) and ((año % 100 != 0) or (año % 400 == 0)):
   
        return f"El año {año} es bisiesto"
    else:
        return f"El año {año} no es bisiesto"

if __name__ == "__main__":
    año = int(input("Ingrese un año: "))
    print(leap_year())
leap_year()
