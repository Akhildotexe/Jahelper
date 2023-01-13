import keyboard
import pyperclip


startKeybind = input(" What key do u want to use for the program to start pasting > ")

def paste_clipboard():
    clipboard_text = pyperclip.paste()
    keyboard.write(clipboard_text)

keyboard.add_hotkey(f"{startKeybind}", paste_clipboard)

while True:
    keyboard.wait()