from tkinter import *
import datetime

startin_time = datetime.datetime.now()

window = Tk()
font = ("monospace", 25,)

str_to_type = """English texts for beginners to practice reading and comprehension online 
and for free. Practicing your comprehension of written English will both improve your 
vocabulary and understanding of grammar and word order. The texts below are designed to 
help you develop while giving you an instant evaluation of your progress.
Prepared by experienced English teachers, the texts, articles and conversations are
 brief and appropriate to your level of proficiency. Take the multiple-choice quiz 
 following each text, and you'll get the results immediately. You will feel both challenged 
 and accomplished! You can even download (as PDF) and print the texts and exercises. 
 It's enjoyable, fun and free. Good luck!"""

str_to_type = str_to_type.split()
typed_word = ""
typed_str = []
uncorrected_entries = 0
current_time = 0


def cal_speed(total_typed_words, uncorrected_errors, time_in_minutes: int = 1):
    all_typed_entries = 0
    for n in total_typed_words:
        all_typed_entries += len(n)
    gross_wpm = (all_typed_entries / 5) / time_in_minutes
    net_wpm = (gross_wpm - (uncorrected_errors / time_in_minutes)) / time_in_minutes
    return net_wpm, gross_wpm


def typing_letters(typed_key):
    global typed_word, typing_area, uncorrected_entries, current_time
    current_time = (datetime.datetime.now() - startin_time).seconds
    current_time = int(current_time)
    if current_time > 60:
        window.quit()

    else:
        uncorrected_entries = 0
        key_touched = typed_key.char

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

# binding typing areca with space and any keypress event

typing_area.bind("<KeyPress>", func=typing_letters)
window.mainloop()

if current_time > 60:
    net_wpm, gross_wpm = cal_speed(uncorrected_errors=uncorrected_entries,
                                   total_typed_words=typed_str,
                                   time_in_minutes=round(current_time / 60))
    print(net_wpm, gross_wpm)
