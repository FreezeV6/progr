def function_zad6 (l1: list, l2: list) -> list:
    return list(x ** 3 for x in list(set(l1 + l2)))