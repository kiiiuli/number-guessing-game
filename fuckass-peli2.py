import random
import tkinter as tk
from tkinter import messagebox


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("jerkmate unranked v2.1")
        self.reset_game()

        self.label = tk.Label(master, text="arvaa kullin koko 1-10cm🍆:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind("<Return>", self.check_guess)

        self.guess_button = tk.Button(master, text="arvaa", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.history_label = tk.Label(master, text="")
        self.history_label.pack()

        self.restart_button = tk.Button(
            master, text="uus peli", command=self.reset_game
        )
        self.restart_button.pack()

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
            self.history_label.config(text=f"arvaukset: {self.guesses}")
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
