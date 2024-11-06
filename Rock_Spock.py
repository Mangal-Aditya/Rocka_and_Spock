from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Rock & Spock")
root.configure(bg="lightpink")



box_width, box_height = 35, 8
final_box_width, final_box_height = 250, 180 



# Set window icon
p1 = PhotoImage(file="download.png")
root.iconphoto(False, p1)

# Title label
name = Label(root, text='Play Rock & Spock with Computer', font="arial", border=20, borderwidth=10, relief="groove")
name.grid(row=0, column=2, padx=10, pady=20)





# Computer images

Rock = Image.open("Rock.jpg").resize((250, 180))
img_Rock = ImageTk.PhotoImage(Rock)
Rock_img = Label(root, image=img_Rock)
Rock_img.grid(row=3, column=0, padx=20, pady=20)

Paper = Image.open("Paper.jpg").resize((250, 180))
img_Paper = ImageTk.PhotoImage(Paper)
Paper_img = Label(root, image=img_Paper)
Paper_img.grid(row=3, column=1, padx=20, pady=20)

Scissors = Image.open("Scissors.jpg").resize((250, 180))
img_Scissors = ImageTk.PhotoImage(Scissors)
Scissors_img = Label(root, image=img_Scissors)
Scissors_img.grid(row=3, column=2, padx=20, pady=20)

Lizard = Image.open("Lizards.jpg").resize((250, 180))
img_Lizard = ImageTk.PhotoImage(Lizard)
Lizard_img = Label(root, image=img_Lizard)
Lizard_img.grid(row=3, column=3, padx=20, pady=20)

Spock = Image.open("Spock.jpg").resize((250, 180))
img_Spock = ImageTk.PhotoImage(Spock)
Spock_img = Label(root, image=img_Spock)
Spock_img.grid(row=3, column=4, padx=20, pady=20)


images = {
    "Rock": img_Rock,
    "Paper": img_Paper,
    "Scissors": img_Scissors,
    "Lizard": img_Lizard,
    "Spock": img_Spock
}




winning_rules = {
    "Rock": ["Scissors", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Lizard": ["Spock", "Paper"],
    "Spock": ["Scissors", "Rock"]
}



def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in winning_rules[player_choice]:
        return "You win!"
    else:
        return "Computer wins!"





def show_message(result):
    # Create a pop-up window for the result
    popup = Toplevel(root)
    popup.title("Game Result")
    popup.geometry("250x150")
    if result == "You win!":
        popup.configure(bg="lightgreen")
        message = Label(popup, text="🎉 You Win! 🎉", font=("Arial", 20), bg="lightgreen", fg="green")
    elif result == "Computer wins!":
        popup.configure(bg="lightcoral")
        message = Label(popup, text="😢 You Lose! 😢", font=("Arial", 20), bg="lightcoral", fg="red")
    else:
        popup.configure(bg="lightblue")
        message = Label(popup, text="😐 It's a Tie! 😐", font=("Arial", 20), bg="lightblue", fg="blue")
    message.pack(expand=True)
    popup.after(2000, popup.destroy) 




def load_image(player_choice):
    # Set user-selected image in "Your Image" box
    image_box_you.config(image=images[player_choice])
    image_box_you.image = images[player_choice]
    image_box_you.config(width=final_box_width, height=final_box_height)
    
    # Randomly select an image for the computer
    computer_choice = random.choice(list(images.keys()))
    image_box.config(image=images[computer_choice])
    image_box.image = images[computer_choice]
    image_box.config(width=final_box_width, height=final_box_height)
    
    # Determine and show the game result
    result = determine_winner(player_choice, computer_choice)
    show_message(result)





# For Computer 
image_box = Label(root, text="Computer Image", font=("Arial", 16), width=20, height=10, borderwidth=2, relief="groove")
image_box.grid(row=4, column=0, padx=30, pady=10,columnspan=2)
image_box.config(width=box_width, height= box_height)

# For You
image_box_you = Label(root, text="Your Image", font=("Arial", 16), width=20, height=10, borderwidth=2, relief="groove")
image_box_you.grid(row=4, column=2, padx=30, pady=10, columnspan=2)
image_box_you.config(width=box_width, height= box_height)

# "Your Options" section
btn_rock = Button(root, text="Rock", command=lambda: load_image("Rock"), image=img_Rock, compound="top")
btn_rock.grid(row=5, column=0, padx=10, pady=10)

btn_paper = Button(root, text="Paper", command=lambda: load_image("Paper"), image=img_Paper, compound="top")
btn_paper.grid(row=5, column=1, padx=10, pady=10)

btn_scissors = Button(root, text="Scissors", command=lambda: load_image("Scissors"), image=img_Scissors, compound="top")
btn_scissors.grid(row=5, column=2, padx=10, pady=10)

btn_lizard = Button(root, text="Lizard", command=lambda: load_image("Lizard"), image=img_Lizard, compound="top")
btn_lizard.grid(row=5, column=3, padx=10, pady=10)

btn_spock = Button(root, text="Spock", command=lambda: load_image("Spock"), image=img_Spock, compound="top")
btn_spock.grid(row=5, column=4, padx=10, pady=10)



root.mainloop()
