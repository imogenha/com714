import tkinter as tk
import customtkinter as ctk


def button_onclick():
    button.configure(text="Clicked!", fg_color="black", text_color="white")


root = tk.Tk()
root.title('test, wow')
root.geometry('600x400+50+50')
root.resizable(False, False)
root.iconbitmap('mas.ico')

message = tk.Label(root, text="Hello, World!")
message.pack()

button = ctk.CTkButton(root, text="Click me!", fg_color="Blue", hover_color="red", text_color="white", corner_radius=5,
                       font=("Arial", 12))

button.configure(command=button_onclick)

button.pack()

root.mainloop()