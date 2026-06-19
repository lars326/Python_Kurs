import tkinter as tk
import random
import time

window = tk.Tk()
window.title("F1 Reaktionstest")
window.geometry("400x300")

start_zeit = 0
bereit = False

def start_test():
    global bereit, start_zeit

    bereit = False
    label.config(text="Warte auf GRÜN...", bg="red")

    # zufällige Wartezeit (wie Startampel)
    wartezeit = random.randint(2000, 5000)
    window.after(wartezeit, gruen_phase)

def gruen_phase():
    global bereit, start_zeit

    label.config(text="JETZT KLICKEN!", bg="green")
    bereit = True
    start_zeit = time.time()

def klicken():
    global bereit

    if not bereit:
        label.config(text="Zu früh! ❌", bg="orange")
        return

    reaktionszeit = time.time() - start_zeit
    label.config(
        text=f"Reaktionszeit: {reaktionszeit:.3f} Sekunden",
        bg="lightblue"
    )
    bereit = False

label = tk.Label(window, text="Drücke Start", font=("Arial", 20), bg="lightgrey")
label.pack(expand=True, fill="both")

button_start = tk.Button(window, text="Start", command=start_test)
button_start.pack(pady=10)

button_klick = tk.Button(window, text="KLICK!", command=klicken)
button_klick.pack(pady=10)

window.mainloop()