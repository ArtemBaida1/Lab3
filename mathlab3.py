num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

def calculate_operations(a, b):
    summa = a + b
    difference = a - b
    product = a * b
    return summa, difference, product

summa, difference, product = calculate_operations(num1, num2)
print(f"Сума: {summa}")
print(f"Різниця: {difference}")
print(f"Добуток: {product}")
