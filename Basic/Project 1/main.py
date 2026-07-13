import random
import customtkinter as ctk

def play_game(human_choice):
    computer = random.choice([-1, 0, 1])
    
    # Dictionaries
    
    human_dictionary = {"s": 1, "w": -1, "g": 0}
    reverse_dictionary = {1: "Snake", -1: "Water", 0: "Gun"}
    human_choice = human_choice.lower()
    human_num = human_dictionary[human_choice]
   
    

    if computer == human_num:
        result="Draw"
    elif computer == -1 and human_num == 1:
        result="You Win!"
    elif computer == -1 and human_num == 0:
        result="You Lose!"
    elif computer == 1 and human_num == -1:
        result="You Lose!"
    elif computer == 1 and human_num == 0:
        result="You Win!"
    elif computer == 0 and human_num == -1:
        result="You Win!"
    elif computer == 0 and human_num == 1:
        result="You Lose!"
    else:
        result="Something Went Wrong"
        
    return reverse_dictionary[computer],reverse_dictionary[human_num],result


def button_clicked(choice):
    computer, human, result = play_game(choice)
    
    computer_label.configure(text=f"Computer: {computer}")
    human_label.configure(text=f"You: {human}")
    result_label.configure(text=f"Result: {result}")
    
app=ctk.CTk()
app.title("Snake Water Gun ")
app.geometry("400x400")
title=ctk.CTkLabel(
    app,
    text="Snake Water GUN",
    font=("Arial",24,"bold")
)   
title.pack(pady=20)
snake_button=ctk.CTkButton(
    app,
    text="🐍Snake",
     width=200,
    command=lambda: button_clicked("s")
)
snake_button.pack(pady=10)

Water_button=ctk.CTkButton(
    app,
    text="🌊Water",
     width=200,
   command=lambda: button_clicked("w")
)
Water_button.pack(pady=10)

Gun_button=ctk.CTkButton(
    app,
    text="🔫Gun",
     width=200,
    command=lambda: button_clicked("g")
)
Gun_button.pack(pady=10)
computer_label = ctk.CTkLabel(app, text="Computer: ")
computer_label.pack(pady=5)

human_label = ctk.CTkLabel(app, text="You: ")
human_label.pack(pady=5)

result_label = ctk.CTkLabel(app, text="Result: ")
result_label.pack(pady=5)
app.mainloop()