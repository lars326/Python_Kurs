import tkinter as tk

window = tk.Tk()
window.title("Lichtschalter")
window.geometry("300x150")
window.config(bg="darkgrey")

licht_an = False
wackelkontakt_an = False
flackern = False

def flackere():
    if flackern:
        aktuelle_farbe = window.cget("bg")

        if aktuelle_farbe == "yellow":
            neue_farbe = "darkgrey"
        else:
            neue_farbe = "yellow"

        window.config(bg=neue_farbe)
        label.config(bg=neue_farbe)

        window.after(150, flackere)

def schalter_klicken():
    global licht_an, flackern

    licht_an = not licht_an

    if licht_an:
        label.config(text="Licht ist AN")
        licht_button.config(text="AUSSCHALTEN")

        if wackelkontakt_an:
            flackern = True
            flackere()
        else:
            window.config(bg="yellow")
            label.config(bg="yellow")
    else:
        flackern = False
        window.config(bg="darkgrey")
        label.config(bg="darkgrey")
        label.config(text="Licht ist AUS")
        licht_button.config(text="EINSCHALTEN")

def wackelkontakt_klicken():
    global wackelkontakt_an

    wackelkontakt_an = not wackelkontakt_an

    if wackelkontakt_an:
        wackel_button.config(text="Wackelkontakt: AN")
    else:
        wackel_button.config(text="Wackelkontakt: AUS")

licht_button = tk.Button(
    window,
    text="EINSCHALTEN",
    command=schalter_klicken,
    width=15
)
licht_button.pack(pady=10)

wackel_button = tk.Button(
    window,
    text="Wackelkontakt: AUS",
    command=wackelkontakt_klicken,
    width=15
)
wackel_button.pack(pady=5)

label = tk.Label(
    window,
    text="Licht ist AUS",
    bg="darkgrey"
)
label.pack(pady=10)

window.mainloop()