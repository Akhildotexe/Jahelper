import tkinter as tk
import pyperclip
import keyboard
import time

root = tk.Tk()
root.geometry("500x500")
root.title("Jahelper")

label = tk.Label(root, text="Jahelper", font=("Helvetica", 30))
label.place(relx=0.5, rely=0.2, anchor='center')

note_label = tk.Label(root, text="Pls note Jahelper will start 2 SECONDS AFTER u click the Start button!")
note_label.place(relx=0.5, rely=0.3, anchor='center')

delay_label = tk.Label(root, text="Above pls specify delay seconds between each letter (recommended is '0.5') ")
delay_label.place(relx=0.5, rely=0.5, anchor='center')

delay_entry = tk.Entry(root, width=5)
delay_entry.insert(0, "0.5")
delay_entry.place(relx=0.5, rely=0.4, anchor='center')


def paste_clipboard():
    time.sleep(2)
    clipboard_text = pyperclip.paste()
    delay_time = float(delay_entry.get())
    for letter in clipboard_text:
        keyboard.press_and_release(letter)
        time.sleep(delay_time)

start_button = tk.Button(root, text="Start", command=paste_clipboard)
start_button.place(relx=0.45, rely=0.6, anchor='center')

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.place(relx=0.59, rely=0.6, anchor='center')

root.mainloop()
