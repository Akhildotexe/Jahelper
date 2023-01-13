import tkinter as tk
import pyperclip
import keyboard
import time

root = tk.Tk()
root.geometry("500x500")
root.title("Jahelper")

label = tk.Label(root, text="Jahelper", font=("Helvetica", 30))
label.place(relx=0.5, rely=0.2, anchor='center')

note_label = tk.Label(root, text="Pls note Jahelper will start 3 SECONDS AFTER u click the Start button!")
note_label.place(relx=0.5, rely=0.3, anchor='center')

def paste_clipboard():
    time.sleep(3)
    clipboard_text = pyperclip.paste()
    keyboard.write(clipboard_text)

start_button = tk.Button(root, text="Start", command=paste_clipboard)
start_button.place(relx=0.45, rely=0.5, anchor='center')

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.place(relx=0.59, rely=0.5, anchor='center')

root.mainloop()



