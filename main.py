from tkinter import *
import datetime

l = datetime.datetime.now()

window = Tk()
font = ("monospace", 25,)

str_to_type = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In porttitor luctus dolor, " \
              "ut tempor eros faucibus eu. Fusce finibus nec elit vitae tincidunt. \n" \
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In porttitor luctus dolor, " \
              "ut tempor eros faucibus eu. Fusce finibus nec elit vitae tincidunt. \n"

str_to_type = str_to_type.split()
typed_word = ""
typed_str = []


def cal_speed(total_typed_words, uncorrected_errors):
    all_typed_entries = 0
    for n in total_typed_words:
        all_typed_entries += len(n)
    gross_wpm = (all_typed_entries / 5) / 1
    net_wpm = (gross_wpm - (uncorrected_errors / 1)) / 1
    return net_wpm, gross_wpm


def sayhi(some):
    global typed_word, typing_area, uncorrected_entries
    current_time = (datetime.datetime.now() - l).seconds
    current_time = int(current_time)
    if current_time > 60:
        window.quit()
    uncorrected_entries = 0
    key_touched = some.char

    if key_touched == ' ':
        typed_str.append(typed_word)
        typed_word = ""
        typing_area.delete(0, END)

    else:
        typed_word += key_touched

    if key_touched == "\x08":
        typed_word = typed_word[:-2]
    elif key_touched == '\x7f':
        typed_word = ""
        typing_area.delete(0, END)

    for n in range(len(typed_str)):
        if typed_str[n] != str_to_type[n]:
            uncorrected_entries += 1


# Text area
text = Text(window)
text.insert(INSERT, " ".join(str_to_type))
text.pack()

# Typing area
typing_area = Entry(width=20, font=font, justify="center")
typing_area.pack()

# binding typing area with space and any keypress event
typing_area.bind("<KeyPress>", func=sayhi)

window.mainloop()

net_wpm, gross_wpm = cal_speed(uncorrected_errors=uncorrected_entries, total_typed_words=typed_str)
print(net_wpm, gross_wpm)
