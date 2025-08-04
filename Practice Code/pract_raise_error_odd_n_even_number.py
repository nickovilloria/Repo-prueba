"""For practicing"""


def check_odd_even(user_input):
    """Odd or even checking function"""
    try:
        somenumber = int(user_input)  # Convert input to an integer
        if somenumber % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    except ValueError as exc:
        raise ValueError(
            "Dato no válido: Por favor ingrese un número entero") from exc


# Example usage
user_input2 = input(
    "Ingrese un Número por favor, ardilla preciosa del corazón: ")
try:
    check_odd_even(user_input2)
except ValueError as e:
    print(e)  # Output if input is invalid
