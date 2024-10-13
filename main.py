import tkinter as tk
from tkinter import messagebox
import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Game Interface")
        self.root.geometry("600x400")
        self.canvas = tk.Canvas(root, width=600, height=300, bg="lightblue")
        self.canvas.pack()

        self.character = self.canvas.create_oval(280, 130, 320, 170, fill="red")
        
        self.command_entry = tk.Entry(root, width=50)
        self.command_entry.pack(pady=20)
        self.command_entry.bind('<Return>', self.on_submit)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.status_label.pack()

    def on_submit(self, event):
        user_input = self.command_entry.get()
        self.command_entry.delete(0, tk.END)
        self.process_command(user_input)

    def process_command(self, command):
     doc = nlp(command.lower())
     action = None

    # Define action keywords
     if "move" in command:
        if "up" in command:
            self.move_character(0, -20)
            self.status_label.config(text="Moved up!")
        elif "down" in command:
            self.move_character(0, 20)
            self.status_label.config(text="Moved down!")
        elif "left" in command:
            self.move_character(-20, 0)
            self.status_label.config(text="Moved left!")
        elif "right" in command:
            self.move_character(20, 0)
            self.status_label.config(text="Moved right!")
        else:
            self.status_label.config(text="Unknown move direction.")
     elif "jump" in command:
        self.jump_character()
        self.status_label.config(text="Jumped!")
     elif "change" in command and "color" in command:
        self.change_color()
        # self.status_label.config(text="Changed color!")
     else:
        self.status_label.config(text="Command not recognized.")


    def move_character(self, dx, dy):
        self.canvas.move(self.character, dx, dy)
        self.status_label.config(text=f"Moved {dx}, {dy}")


    def jump_character(self):
    # Move the character up
        self.canvas.move(self.character, 0, -50)
        self.status_label.config(text="Jumped!")
        self.root.update()  # Update the GUI to reflect the upward move immediately

    # Move the character back down after 200ms (delay for the jump)
        self.root.after(200, lambda: self.canvas.move(self.character, 0, 50))

    def change_color(self):
        # List of colors to cycle through
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "brown", "pink", "black", "white"]
        
        # Get the current color of the character
        current_color = self.canvas.itemcget(self.character, 'fill')
        
        # Find the index of the current color in the list, then get the next color
        current_index = colors.index(current_color)
        new_color = colors[(current_index + 1) % len(colors)]  # Cycle through colors
        
        # Change the color of the character
        self.canvas.itemconfig(self.character, fill=new_color)
        self.status_label.config(text=f"Color changed to {new_color}!")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()