def calculate_parallelepiped(width, length, height):
    volume = width * length * height
    surface_area = 2 * (width * length + width * height + length * height)
    return volume, surface_area

width = float(input("Введіть ширину: "))
length = float(input("Введіть довжину: "))
height = float(input("Введіть висоту: "))

volume, surface_area = calculate_parallelepiped(width, length, height)
print(f"Об'єм: {volume}")
print(f"Площа поверхні: {surface_area}")