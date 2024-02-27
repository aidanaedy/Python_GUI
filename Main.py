from tkinter import *

# Create the main window
window = Tk()
window.title("Aidan's UI Window")

# Add a label widget
label = Label(window, text="Hello, Aidan!")
label.pack()

# Add a button widget
button = Button(window, text="Click Me!", command=lambda: label.config(text="Clicked!"))
button.pack()

# Start the event loop
window.mainloop()
