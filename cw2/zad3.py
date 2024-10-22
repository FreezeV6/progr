def function_zad3 (num1: int) -> bool:
    return bool(num1 % 2 == 0)

out = function_zad3(8)
print("Liczba parzysta" if out else "Liczba nieparzysta")