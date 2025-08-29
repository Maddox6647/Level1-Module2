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
        self.label = tk.Label(self, bg='gray', text='', font=('arial', 50, 'normal'))
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.4)


        self.button1 = tk.Button(self, text='1', fg='black', font=('arial', 16, 'bold'), command=self.on_button1_press)
        self.button1.place(relx=0.1, rely=0.5, relwidth=0.1, relheight=0.15)

        self.button2 = tk.Button(self, text='2', fg='black', font=('arial', 16, 'bold'), command=self.on_button2_press)
        self.button2.place(relx=0.2, rely=0.5, relwidth=0.1, relheight=0.15)

        self.button3 = tk.Button(self, text='3', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button3.place(relx=0.3, rely=0.5, relwidth=0.1, relheight=0.15)

        self.button4 = tk.Button(self, text='4', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button4.place(relx=0.4, rely=0.5, relwidth=0.1, relheight=0.15)

        self.button5 = tk.Button(self, text='5', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button5.place(relx=0.5, rely=0.5, relwidth=0.1, relheight=0.15)

        self.button6 = tk.Button(self, text='6', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button6.place(relx=0.6, rely=0.5, relwidth=0.1, relheight=0.15)

        self.button7 = tk.Button(self, text='7', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button7.place(relx=0.7, rely=0.5, relwidth=0.1, relheight=0.15)

        self.button8 = tk.Button(self, text='8', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button8.place(relx=0.8, rely=0.5, relwidth=0.1, relheight=0.15)

        self.button9 = tk.Button(self, text='9', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button9.place(relx=0.1, rely=0.65, relwidth=0.1, relheight=0.15)

        self.button10 = tk.Button(self, text='0', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button10.place(relx=0.2, rely=0.65, relwidth=0.1, relheight=0.15)

        self.button11 = tk.Button(self, text='+', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button11.place(relx=0.3, rely=0.65, relwidth=0.1, relheight=0.15)

        self.button12 = tk.Button(self, text='-', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button12.place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.15)

        self.button13 = tk.Button(self, text='/', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button13.place(relx=0.5, rely=0.65, relwidth=0.1, relheight=0.15)

        self.button14 = tk.Button(self, text='x', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button14.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.15)

        self.button15 = tk.Button(self, text='=', fg='black', font=('arial', 16, 'bold'), command=self.on_button_press)
        self.button15.place(relx=0.7, rely=0.65, relwidth=0.1, relheight=0.15)




        # Add a text field that can take input from the user
        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.1, rely=0.8, relwidth=80, height=180)

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
        self.button1.bind('<ButtonRelease>', self.on_button_release)
        self.button2.bind('<ButtonRelease>', self.on_button_release)
        self.button3.bind('<ButtonRelease>', self.on_button_release)
        self.button4.bind('<ButtonRelease>', self.on_button_release)
        self.button5.bind('<ButtonRelease>', self.on_button_release)
        self.button6.bind('<ButtonRelease>', self.on_button_release)
        self.button7.bind('<ButtonRelease>', self.on_button_release)
        self.button8.bind('<ButtonRelease>', self.on_button_release)
        self.button9.bind('<ButtonRelease>', self.on_button_release)
        self.button10.bind('<ButtonRelease>', self.on_button_release)
        self.button11.bind('<ButtonRelease>', self.on_button_release)
        self.button12.bind('<ButtonRelease>', self.on_button_release)
        self.button13.bind('<ButtonRelease>', self.on_button_release)
        self.button14.bind('<ButtonRelease>', self.on_button_release)
        self.button15.bind('<ButtonRelease>', self.on_button_release)
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

    def on_button1_press(self):
        print("I pressed button 1")

    def on_button2_press(self):
        print("I pressed button 2")

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
        self.label.configure(bg='gray')

    def mouse_leave_label(self, event):
        print(repr(event))
        print('  x ...: ' + str(event.x))
        print('  y ...: ' + str(event.y))
        self.label.configure(bg='gray')


if __name__ == '__main__':
    app = ButtonsAndTextFields()
    app.title('Calculator')
    app.geometry('900x900')
    app.mainloop()
