"""
Create a simple calculator app
"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label

class ButtonsAndTextFields(tk.Tk):
    def __init__(self):
        super().__init__()

        # Add a label
        self.label = tk.Label(self, bg='green', font=('Rockwell', 20, 'normal', 'underline'))
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)


        self.button = tk.Button(self, text='1   2   3   4   5   6   7   8   9   0'
                                           '/  *  -  +  square root', fg='blue',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)

        # Add a text field that can take input from the user
        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.1, rely=0.8, relwidth=0.8, height=18)

        # bind(event, handler) says to call the handler (function or method)
        # when an event occurs. The events are predefined by tkinter.
        # common events: https://www.tcl.tk/man/tcl8.6/TkCmd/bind.htm#M7
        #   <KeyPress>      - a keyboard key is pressed
        #   <KeyRelease>    - a keyboard key is released
        #   <ButtonPress>   - a mouse button is pressed
        #   <ButtonRelease> - a mouse button is released
        #   <Enter>         - the mouse has entered the object
        #   <Leave>         - the mouse has left the object
        #   <Motion>        - the mouse has moved within the object
        self.text_field.bind('<KeyPress>', self.on_text_entry)

        # bind() can also be used in conjunction with the command= option
        self.button.bind('<ButtonRelease>', self.on_button_release)

        # bind() used to change background of the label as the mouse enters
        # and leaves the label object
        self.label.bind('<Enter>', self.mouse_enter_label)
        self.label.bind('<Leave>', self.mouse_leave_label)

    def on_button_press(self):
        # Get the text from the text field and store into a variable
        text_in_text_field = self.text_field.get()

        # Update the text in the label
        self.label.configure(text=text_in_text_field)

        messagebox.showinfo(None, 'sorry the calc is still a work in progress')

    def on_text_entry(self, event):
        print(repr(event))
        print('  keycode ..: ' + str(event.keycode))
        print('  char: ....: ' + event.char)
        print('  keysym ...: ' + str(event.keysym))

    def on_button_release(self, event):
        print(repr(event))
        print('  num ...: ' + str(event.num) + ' (button number)')

    def on_button_press2(self, event):
        print(repr(event))
        print('  num ...: ' + str(event.num) + ' (button number)')

    def mouse_enter_label(self, event):
        print(repr(event))
        print('  x ...: ' + str(event.x))
        print('  y ...: ' + str(event.y))
        self.label.configure(bg='yellow')

    def mouse_leave_label(self, event):
        print(repr(event))
        print('  x ...: ' + str(event.x))
        print('  y ...: ' + str(event.y))
        self.label.configure(bg='green')


if __name__ == '__main__':
    app = ButtonsAndTextFields()
    app.title('Calculator')
    app.geometry('900x900')
    app.mainloop()
