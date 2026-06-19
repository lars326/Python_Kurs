import math

while True:
    try:
        radius = float(input("Radius eingeben: "))

        if radius > 0:
            break
        else:
            print("Der Radius muss positiv sein.")

    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")

d = 2 * radius
u = 2 * math.pi * radius
a = math.pi * radius ** 2

print("Durchmesser:", d)
print("Umfang:", u)
print("Fläche:", a)