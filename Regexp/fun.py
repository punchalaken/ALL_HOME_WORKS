import tkinter as tk
def s1():
    def funny():
        message = "Спасибо за уделенное время моему домашнему заданию =)"
        label.config(text=message, fg='#FFA500', bg="black")

    root = tk.Tk()
    root.title("Блогодарственное письмо")
    label_font = ("Helvetica", 25)
    label = tk.Label(root, text="Добрый день!", font=label_font)
    label.pack()
    button_font = ("Helvetica", 25)
    button = tk.Button(root, text="Пожалуйста, нажмите сюда", font=button_font, command=funny)
    button.pack()
    root.mainloop()