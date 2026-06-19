import tkinter as tk

window = tk.Tk()
window.title(string="Meine tolle GUI")
window.configure(bg="yellow")
window.minsize(width=200, height=200)
window.maxsize(width=500, height=500)


widgets=[
    tk.Label, tk.Checkbutton, tk. Entry, tk.Button, tk.Radiobutton, tk. Scale, tk.Spinbox
]

for widget in widgets:
    try:
        w = widget(window, text=widget.__name__)
    except tk.TclError:
        w = widget(window)
        
    w.pack(padx=5, pady=5, fill="x")
    
window.mainloop()