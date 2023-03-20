from tkinter import Tk, Label, Entry
from tkinter import *

window = Tk()
font = ("monospace", 25,)

to_type = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In porttitor luctus dolor, " \
          "ut tempor eros faucibus eu. Fusce finibus nec elit vitae tincidunt. \n" \
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In porttitor luctus dolor, " \
          "ut tempor eros faucibus eu. Fusce finibus nec elit vitae tincidunt. \n"

checker_str = ""


def sayhi(some):
    global checker_str
    typed_keys = str(some.keysym)

    if some.keysym != "space":
        checker_str += typed_keys

        #       text_area.config(foreground="red")
    else:
        checker_str += " "

    current_length = len(checker_str)
    if checker_str[current_length-1] == to_type[ current_length-1]:
        text.tag_config("start", foreground="green")
        text.tag_add("start", 1.0, float(f"1.{current_length}"))
    else:
        text.tag_config("start", foreground="red")
        text.tag_add("start", float(f"1.{current_length -1}"), float(f"1.{current_length}"))
    # print(checker_str)


# Text area
# text_area = Label(text=to_type, font=font, wraplength=900, )
# text_area.pack(pady=100)
text = Text(window)
text.insert(INSERT, to_type)
text.pack()
# Typing area
typing_area = Entry(width=20, font=font, justify="center")
typing_area.pack()
# binding typing area with space and any keypress event
#yping_area.bind("<space>", func=sayhi)
typing_area.bind("<KeyPress>", func=sayhi)
window.mainloop()
