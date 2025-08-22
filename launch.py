import random
import tkinter as tk

import os


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("jerkmate unranked v2.1")
        self.reset_game()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(script_dir, "jerkmate.png")
        self.bg_img = tk.PhotoImage(file=img_path)
        self.bg_label = tk.Label(master, image=self.bg_img)
        self.bg_label.place(x=1, y=1, relwidth=1, relheight=1)

        self.label = tk.Label(master, text="arvaa kullin koko 1-10cm🍆:", bg="#ffffff")
        self.label.place(x=20, y=10)

        self.entry = tk.Entry(master)
        self.entry.place(x=20, y=40, width=100)
        self.entry.bind("<Return>", self.check_guess)

        self.guess_button = tk.Button(master, text="arvaa", command=self.check_guess)
        self.guess_button.place(x=130, y=38)

        self.result_label = tk.Label(master, text="", bg="#ffffff")
        self.result_label.place(x=20, y=70)

        self.history_label = tk.Label(master, text="", bg="#ffffff")
        self.history_label.place(x=20, y=100)

        self.restart_button = tk.Button(
            master, text="uus peli", command=self.reset_game
        )
        self.restart_button.place(x=200, y=38)

    def reset_game(self):
        self.number = random.randint(1, 10)
        self.guesses = []
        if hasattr(self, "result_label"):
            self.result_label.config(text="")
            self.history_label.config(text="")
        if hasattr(self, "entry"):
            self.entry.delete(0, tk.END)

    def check_guess(self, event=None):
        guess_str = self.entry.get()
        try:
            guess = int(guess_str)
        except ValueError:
            self.result_label.config(text="syötä numero daiju")
            return

        self.guesses.append(guess)
        if guess == self.number:
            self.result_label.config(text="🎉 Gz arvasit vihu kulli oikei@@@")
            self.history_label.config(text=f"yritystä: {len(self.guesses)}")
        elif guess < self.number:
            self.result_label.config(text="iha hyvä kokone mut isompi⬆️")
        else:
            self.result_label.config(text="ei nyt hulluuksii mennä, pienempi⬇️")

        self.entry.delete(0, tk.END)


window = tk.Tk()
window.geometry("300x150")
game = NumberGuessingGame(window)
window.resizable(False, False)
window.mainloop()
