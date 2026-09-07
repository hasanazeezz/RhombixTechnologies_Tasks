import tkinter as tk
import random

window = tk.Tk()
window.title("Memory Puzzle Game")
window.geometry("500x550")

# Cards - each fruit appears twice
cards = [
    "🍎", "🍎",
    "🍌", "🍌",
    "🍇", "🍇",
    "🍓", "🍓",
    "🍉", "🍉",
    "🍒", "🍒",
    "🥝", "🥝",
    "🍍", "🍍"
]

random.shuffle(cards)

buttons = []

first_card = None
second_card = None

score = 0
pairs = 0
time = 60
game_over = False


def click_card(number):

    global first_card
    global second_card

    if game_over:
        return

    if buttons[number]["state"] == "disabled":
        return

    if first_card == number:
        return

    buttons[number]["text"] = cards[number]

    if first_card is None:
        first_card = number

    else:
        second_card = number

        window.after(500, check_cards)


def check_cards():

    global first_card
    global second_card
    global score
    global pairs

    if cards[first_card] == cards[second_card]:

        buttons[first_card]["state"] = "disabled"
        buttons[second_card]["state"] = "disabled"

        score = score + 10
        pairs = pairs + 1

        score_label["text"] = "Score: " + str(score)

        if pairs == 8:
            win_game()

    else:

        buttons[first_card]["text"] = "?"
        buttons[second_card]["text"] = "?"

    first_card = None
    second_card = None


def timer():

    global time
    global game_over

    if time > 0 and pairs < 8:

        time = time - 1
        timer_label["text"] = "Time: " + str(time)

        window.after(1000, timer)

    elif time == 0:

        game_over = True
        message_label["text"] = "Game Over! Time is up!"


def win_game():

    global game_over

    game_over = True
    message_label["text"] = "Congratulations! You won!"


title_label = tk.Label(
    window,
    text="Memory Puzzle Game",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=10)


# Score and timer
score_label = tk.Label(
    window,
    text="Score: 0",
    font=("Arial", 14)
)

score_label.pack()

timer_label = tk.Label(
    window,
    text="Time: 60",
    font=("Arial", 14)
)

timer_label.pack()

message_label = tk.Label(
    window,
    text="Match all the pairs!",
    font=("Arial", 13)
)

message_label.pack(pady=10)


game_frame = tk.Frame(window)
game_frame.pack()

for i in range(16):

    button = tk.Button(
        game_frame,
        text="?",
        font=("Arial", 20),
        width=5,
        height=2,
        command=lambda i=i: click_card(i)
    )

    button.grid(
        row=i // 4,
        column=i % 4,
        padx=5,
        pady=5
    )

    buttons.append(button)


timer()

window.mainloop()

