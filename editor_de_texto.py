# 
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath: 
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open file: {filepath}")

def save_file(window, text_edit):
    file = asksaveasfile(filetypes=[("Text Files", "*.txt")])

    if not file:
        return
    filepath = file.name
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open file: {filepath}")


def main():
    window = tk.Tk()
    window.title("Editor de Texto")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)
    # Widgets
    text_edit = tk.Text(window, font="Helvetica 18", bg="black", fg="white")  # Set background to black and foreground (text color) to white
    text_edit.grid(row=0, column=1)
    
    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Ahorrar", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Abierto", command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    # Bind commands with keyboard
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()

main()    
