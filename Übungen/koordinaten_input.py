ost = int(input("Ostwert eingeben: "))
nord = int(input("Nordwert eingeben: "))

O_formatiert = f"{ost:,.0f}".replace(",", "'")
N_formatiert = f"{nord:,.0f}".replace(",", "'")

print(f"E {O_formatiert} / N {N_formatiert}")

if 2480000 <= ost <= 2840000 and 1070000 <= nord <= 1300000:
      print("liegt innerhalb der Schweiz.")
else:
    print("liegt ausserhalb der Schweiz.")
            