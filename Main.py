from tkinter import *

# Create the main window
window = Tk()
window.title("Aidan's UI Window")


# Define functions for the button options
def button_click():
    print("Button Clicked!")


# Add a label
label = Label(window, text="Hello, Aidan!")
label.pack()

# Add a button with a defined function
button = Button(window, text="Click Me!", command=button_click)
button.pack()

# Start the event loop
window.mainloop()
