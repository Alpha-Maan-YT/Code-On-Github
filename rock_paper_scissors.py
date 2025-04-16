import tkinter as tk
import random

# Initialize score
score = 5


# Function to play the game and update score
def play(choice):
    global score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    result = ""
    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
            (choice == "Paper" and computer_choice == "Rock") or \
            (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"
        score -= 1  # Decrease score on loss

    if score == 0:
        result = "Game Over! You Lost!"

    label_result.config(text=f"Computer: {computer_choice}\n{result}")
    label_score.config(text=f"Score: {score}")


# Set up the main Tkinter window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Create and place buttons
buttons_frame = tk.Frame(root)
buttons_frame.pack()

for option in ["Rock", "Paper", "Scissors"]:
    tk.Button(buttons_frame, text=option, width=10, command=lambda opt=option: play(opt)).pack(side="left", padx=5,
                                                                                               pady=5)

# Score label
label_score = tk.Label(root, text=f"Score: {score}", font=("Arial", 12))
label_score.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Choose an option!", font=("Arial", 12))
label_result.pack(pady=10)

# Run the Tkinter loop
root.mainloop()