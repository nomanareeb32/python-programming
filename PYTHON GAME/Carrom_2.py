import tkinter as tk
import random


class CarromGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Carrom Game")

        # create the game board
        self.canvas = tk.Canvas(self.master, width=600, height=600, bg="white")
        self.canvas.pack()
        self.canvas.create_oval(50, 50, 550, 550, outline="black", width=2)
        self.canvas.create_oval(150, 150, 450, 450, outline="black", width=2)
        self.canvas.create_oval(250, 250, 350, 350, outline="black", width=2)
        self.canvas.create_line(300, 50, 300, 150, fill="black", width=2)
        self.canvas.create_line(300, 450, 300, 550, fill="black", width=2)
        self.canvas.create_line(50, 300, 150, 300, fill="black", width=2)
        self.canvas.create_line(450, 300, 550, 300, fill="black", width=2)

        # create the coins
        self.white_coins = []
        for i in range(9):
            x = random.randint(100, 500)
            y = random.randint(100, 500)
            self.white_coins.append(
                self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white", outline="black", width=2))
        self.black_coins = []
        for i in range(9):
            x = random.randint(100, 500)
            y = random.randint(100, 500)
            self.black_coins.append(
                self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="black", outline="white", width=2))
        x = random.randint(100, 500)
        y = random.randint(100, 500)
        self.red_coin = self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="red", outline="black", width=2)

        # set up the game state
        self.player = random.choice(['Player 1', 'Player 2'])
        self.white_coins_left = 9
        self.black_coins_left = 9
        self.red_coin_left = True

        # create the player labels
        self.player_label = tk.Label(self.master, text=f"It's {self.player}'s turn", font=("Arial", 16))
        self.player_label.pack(pady=20)

        # create the input box and button
        self.input_box = tk.Entry(self.master, font=("Arial", 16))
        self.input_box.pack(pady=20)
        self.input_box.focus_set()
        self.shoot_button = tk.Button(self.master, text="Shoot", font=("Arial", 16), command=self.shoot)
        self.shoot_button.pack(pady=20)

        # create the score labels
        self.white_score_label = tk.Label(self.master, text=f"White Coins: {self.white_coins_left}", font=("Arial", 16))
        self.white_score_label.pack(side="left", padx=20, pady=10)
        self.black_score_label = tk.Label(self.master, text=f"Black Coins: {self.black_coins_left}", font=("Arial", 16))
        self.black
