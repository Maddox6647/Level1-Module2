"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.Resampling.LANCZOS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos
"""
These are the photos:
EX5MfJfXgAE65jh.jpg, sddefault.jpg, sad.jpeg
"""
# TODO 1) Create a new tkinter class
class PhotoQuiz(tk.Tk):
    # TODO 2) Create a constructor
    def __init__(self):
        # TODO 3) call Tk's constructor
        super().__init__()
        # TODO 4) Create a member variable for a label and place it.
        #  You do not need to add any text or images to the label.
        self.photo_label = tk.Label(self)
        self.photo_label.pack()

# TODO 5) Create an if __name__ == '__main__': block
if __name__ == '__main__':
    # TODO 6) Create an object of the tkinter class
    shrek = PhotoQuiz()
    # TODO 7) Set the app window width and height using geometry()
    shrek.geometry("500x500")
    # TODO 8) Declare and initialize a score variable
    score = 0
    # TODO 9) Create an image object variable using the create_image function
    #  above and store it in a variable

    bobby = create_image("EX5MfJfXgAE65jh.jpg", 400, 400)
    # TODO 10) Set the image onto the class's label using the configure method,
    #  for example:
    #  app.photo_label.configure(image=image_object)
    shrek.photo_label.configure(image=bobby)
    shrek.photo_label.image = bobby
    # TODO 11) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.
    boblikesmen = simpledialog.askstring("Question 1", "which meme is this?")
    # TODO 12) If the answer is correct, increase the score by 1
    if boblikesmen and boblikesmen.lower() == "shrek wazowski":
        score += 1
    else:
        messagebox.showinfo("sfhdsh", "Now how'd you end up here?")
    # TODO 13) Repeat the steps to show a different photo and ask a different
    #  question
    shreklikesmen = create_image("sddefault.jpg", 400, 400)
    shrek.photo_label.configure(image=shreklikesmen)
    shrek.photo_label.image = shreklikesmen
    shrek.update()
    answer2 = simpledialog.askstring("Question 2", "which variation of amogus meme is this?")
    if answer2 and answer2.lower() == "mogus":
        score += 1
    else:
        messagebox.showinfo("sfhdsh", "sad")
    williambeckwith = create_image("sad.jpg", 400, 400)
    shrek.photo_label.configure(image=williambeckwith)
    shrek.photo_label.image = williambeckwith
    shrek.update()
    answer3 = simpledialog.askstring("Question 3", "which meme is this?")
    if answer3 and answer3.lower() == "amogus":
        score += 1
    else:
        messagebox.showinfo("sfhdsh", "womp womp")
    # TODO 14) Display the score to the user after asking the last question
messagebox.showinfo("Score", "You got " + str(score) + " out of 3!")

shrek.mainloop()
