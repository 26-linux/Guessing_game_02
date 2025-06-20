import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess the Number!")
        self.root.geometry("450x300")
        self.root.configure(bg="#d0e6f7")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(root, text="🎉 Welcome to the Guessing Game!", font=("Comic Sans MS", 16, "bold"), bg="#d0e6f7", fg="#2b2d42")
        self.title_label.pack(pady=10)

        self.instruction = tk.Label(root, text="I have picked a number between 1 and 100.\nCan you guess what it is?", font=("Arial", 12), bg="#d0e6f7")
        self.instruction.pack()

        self.entry = tk.Entry(root, font=("Arial", 14), justify='center')
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12), bg="#5e60ce", fg="white", width=15)
        self.button.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#d0e6f7", fg="#ef476f")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game, font=("Arial", 11), bg="#06d6a0", fg="white")
        self.reset_button.pack(pady=5)
        self.reset_button.config(state="disabled")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try a higher number 🔼")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try a lower number 🔽")
            else:
                self.result_label.config(text=f"🎯 Correct! You guessed it in {self.attempts} attempts!")
                self.button.config(state="disabled")
                self.reset_button.config(state="normal")
        except ValueError:
            self.result_label.config(text="🚫 Please enter a valid number!")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.button.config(state="normal")
        self.reset_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
